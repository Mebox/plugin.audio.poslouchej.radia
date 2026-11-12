"""
 *  Copyright (C) 2026
 *  This file is part of plugin.audio.poslouchej.radia
 *
 *  SPDX-License-Identifier: GPL-2.0-only
 *  See LICENSE.txt for more information.
"""

import sys
import os
import json
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import xbmcvfs
import socket
import urllib.parse
import time
import threading
import hashlib
import base64
import xml.etree.ElementTree as ET

from resources.lib.api import RadioApi, CACHE_DIR, KEYS

ADDON            = xbmcaddon.Addon(id='plugin.audio.poslouchej.radia')
ADDON_NAME       = ADDON.getAddonInfo('name')
ADDON_ICON       = ADDON.getAddonInfo('icon')
ADDON_FANART     = ADDON.getAddonInfo('fanart')
ADDON_PATH       = xbmcvfs.translatePath(ADDON.getAddonInfo('path'))
LANG             = ADDON.getLocalizedString
USER_DATA_FOLDER = xbmcvfs.translatePath(
    "special://profile/addon_data/plugin.audio.poslouchej.radia/")

HANDLE   = int(sys.argv[1])
BASE_URL = sys.argv[0]

radio_api      = RadioApi()
_dead_hosts    = {}
_DEAD_HOST_TTL = 120

_TOP_SEED       = b'poslouchej.radia/top/v1'
_TOP_BLOB       = 'DO8dWlSXsy/LY3tS9j1NlhyMVSqMzPUez40fALDLy/v5Tg=='


def _unmask():
    raw = base64.b64decode(_TOP_BLOB)
    out, i = b'', 0
    while len(out) < len(raw):
        out += hashlib.sha256(_TOP_SEED + i.to_bytes(4, 'big')).digest()
        i += 1
    return bytes(a ^ b for a, b in zip(raw, out)).decode('ascii')


DEFAULT_TOP_URL = _unmask()
LISTEN_SECONDS  = 300
TOP_CACHE_TTL   = 900


def _url(route, **params):
    return BASE_URL + '?' + urllib.parse.urlencode({'route': route, **params})


def _apply_advancedsettings():
    path = xbmcvfs.translatePath('special://masterprofile/advancedsettings.xml')
    try:
        root = ET.parse(path).getroot() if xbmcvfs.exists(path) else ET.Element('advancedsettings')
    except Exception:
        root = ET.Element('advancedsettings')
    tree = ET.ElementTree(root)
    sec = root.find('musicplayer')
    if sec is None:
        sec = ET.SubElement(root, 'musicplayer')
    for el in sec.findall('queuedepth'):
        sec.remove(el)
    ET.SubElement(sec, 'queuedepth').text = '1'
    try:
        tree.write(path, encoding='utf-8', xml_declaration=True)
    except Exception as e:
        xbmc.log('[poslouchej.radia] advancedsettings write failed: {}'.format(e), xbmc.LOGWARNING)


def _stream_ok(url, timeout=3):
    try:
        p    = urllib.parse.urlparse(url)
        host = p.hostname
        port = p.port or (443 if p.scheme == 'https' else 80)
        if not host:
            return False

        key = '{}:{}'.format(host, port)
        now = time.time()
        if key in _dead_hosts and now - _dead_hosts[key] < _DEAD_HOST_TTL:
            return False

        req_path = p.path or '/'
        if p.query:
            req_path += '?' + p.query

        request = (
            'GET {path} HTTP/1.0\r\n'
            'Host: {host}\r\n'
            'User-Agent: Mozilla/5.0\r\n'
            'Icy-MetaData: 1\r\n'
            'Connection: close\r\n'
            '\r\n'
        ).format(path=req_path, host=host).encode('utf-8')

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
            if s.connect_ex((host, port)) != 0:
                s.close()
                _dead_hosts[key] = now
                return False

            if p.scheme == 'https':
                import ssl
                try:
                    ctx = ssl.create_default_context()
                    s = ctx.wrap_socket(s, server_hostname=host)
                except ssl.SSLError:
                    _dead_hosts[key] = now
                    return False

            s.sendall(request)

            first_line = b''
            while len(first_line) < 128:
                ch = s.recv(1)
                if not ch or ch == b'\n':
                    break
                first_line += ch
            first_line = first_line.strip()
        finally:
            try:
                s.close()
            except Exception:
                pass

        if not first_line:
            _dead_hosts[key] = now
            return False

        if first_line.upper().startswith(b'ICY '):
            xbmc.log(
                '[poslouchej.radia] ShoutCast v1 (ICY) stream odmítnut - '
                'Kodi ho neumí přehrát: {}'.format(url),
                xbmc.LOGWARNING
            )
            _dead_hosts[key] = now
            return False

        parts = first_line.split(b' ', 2)
        if len(parts) >= 2:
            try:
                status = int(parts[1])
                if status >= 400:
                    _dead_hosts[key] = now
                    return False
            except ValueError:
                pass

        return True

    except Exception:
        return False


def _fav_file():
    os.makedirs(USER_DATA_FOLDER, exist_ok=True)
    path = USER_DATA_FOLDER + 'myFav.json'
    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as f:
            f.write('{"stanice": []}')
    return path


def _load_fav():
    path = _fav_file()
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data.get('stanice'), list):
            raise ValueError('bad format')
        return data
    except Exception as e:
        xbmc.log('[poslouchej.radia] myFav.json nelze číst: {}'.format(e), xbmc.LOGWARNING)
        return {'stanice': []}


def _save_fav(data):
    with open(_fav_file(), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)


def _stats_file():
    os.makedirs(USER_DATA_FOLDER, exist_ok=True)
    return USER_DATA_FOLDER + 'stats.json'


def _load_stats():
    try:
        with open(_stats_file(), 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError('bad format')
        return data
    except Exception:
        return {}


def _count_play(url, name, img):
    data = _load_stats()
    st = data.get(url) or {'count': 0}
    st.update({'title': name, 'img': img, 'count': int(st.get('count', 0)) + 1,
               'last': int(time.time())})
    data[url] = st
    try:
        tmp = _stats_file() + '.tmp'
        with open(tmp, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)
        os.replace(tmp, _stats_file())
    except Exception as e:
        xbmc.log('[poslouchej.radia] stats.json nelze zapsat: {}'.format(e), xbmc.LOGWARNING)


def _top_url():
    return (ADDON.getSetting('top_url') or '').strip() or DEFAULT_TOP_URL


def _hash(url):
    return hashlib.sha1(url.encode('utf-8')).hexdigest()


def _send_hit(url):
    base = _top_url()
    if not base or ADDON.getSetting('send_stats') == 'false':
        return
    try:
        import requests
        requests.post(base, data={'action': 'hit', 'h': _hash(url)},
                      headers={'User-Agent': 'Kodi-poslouchej.radia'}, timeout=8)
    except Exception as e:
        xbmc.log('[poslouchej.radia] odeslani statistiky selhalo: {}'.format(e.__class__.__name__),
                 xbmc.LOGWARNING)


def _track_listening(url, name, img):
    monitor, player = xbmc.Monitor(), xbmc.Player()

    def _is_ours():
        try:
            return (player.isPlayingAudio()
                    and player.getPlayingFile().split('|')[0] == url)
        except RuntimeError:
            return False

    waited = 0
    while not _is_ours():
        if monitor.waitForAbort(1) or waited >= 30:
            return
        waited += 1
    listened = 0
    while listened < LISTEN_SECONDS:
        if monitor.waitForAbort(5) or not _is_ours():
            return
        if not xbmc.getCondVisibility('Player.Paused'):
            listened += 5
    xbmc.log('[poslouchej.radia] poslech {} s: {}'.format(LISTEN_SECONDS, name), xbmc.LOGINFO)
    _count_play(url, name, img)
    _send_hit(url)


def _fetch_top():
    base = _top_url()
    if not base:
        return None
    cache = USER_DATA_FOLDER + 'top_cache.json'

    def _read_cache():
        try:
            with open(cache, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return None

    if os.path.exists(cache) and time.time() - os.path.getmtime(cache) < TOP_CACHE_TTL:
        rows = _read_cache()
        if rows:
            return rows
    try:
        import requests
        r = requests.get(base, params={'action': 'top', 'limit': 100},
                         headers={'User-Agent': 'Kodi-poslouchej.radia'}, timeout=8)
        r.raise_for_status()
        txt = r.text
        rows = json.loads(txt[txt.index('['):txt.rindex(']') + 1])
        if not isinstance(rows, list):
            raise ValueError('neplatna data')
        os.makedirs(USER_DATA_FOLDER, exist_ok=True)
        with open(cache, 'w', encoding='utf-8') as f:
            json.dump(rows, f)
        return rows
    except Exception as e:
        xbmc.log('[poslouchej.radia] nacteni TOP selhalo: {}'.format(e.__class__.__name__),
                 xbmc.LOGWARNING)
        return _read_cache()


def show_top_listened():
    rows = _fetch_top()
    stations = []
    if rows:
        by_hash = {}
        for key in KEYS:
            if not _visible(key):
                continue
            for st in radio_api._get(key) or []:
                by_hash.setdefault(_hash(st['url']), st)
        for r in rows:
            st = by_hash.get(r.get('h'))
            if st:
                stations.append(dict(st, count=int(r.get('c', 0))))
        stations = stations[:50]
    else:
        data = _load_stats()
        top = sorted(data.items(), key=lambda kv: (-int(kv[1].get('count', 0)),
                                                   -int(kv[1].get('last', 0))))[:50]
        for url, st in top:
            stations.append({'title': st.get('title', ''), 'url': url,
                             'img': st.get('img') or ADDON_ICON,
                             'count': int(st.get('count', 0))})
    _stations(stations)


def _media(name):
    return os.path.join(ADDON_PATH, 'resources', 'media', name)


def _add_dir(label, url, icon=None):
    li = xbmcgui.ListItem(label)
    if icon:
        li.setArt({'icon': icon, 'thumb': icon, 'fanart': ADDON_FANART})
    else:
        li.setArt({'icon': ADDON_ICON, 'fanart': ADDON_FANART})
    xbmcplugin.addDirectoryItem(HANDLE, url, li, isFolder=True)


def _report_dead(url, name):
    base = _top_url()
    if not base or ADDON.getSetting('send_stats') == 'false':
        return
    h, now = _hash(url), time.time()
    path = USER_DATA_FOLDER + 'dead_reported.json'
    try:
        with open(path, 'r', encoding='utf-8') as f:
            seen = json.load(f)
    except Exception:
        seen = {}
    if now - seen.get(h, 0) < 86400:
        return
    seen = {k: v for k, v in seen.items() if now - v < 86400}
    seen[h] = now
    try:
        os.makedirs(USER_DATA_FOLDER, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(seen, f)
        import requests
        requests.post(base, data={'action': 'dead', 'h': h, 'title': (name or '')[:80]},
                      headers={'User-Agent': 'Kodi-poslouchej.radia'}, timeout=5)
    except Exception as e:
        xbmc.log('[poslouchej.radia] hlaseni mrtveho streamu selhalo: {}'.format(e.__class__.__name__),
                 xbmc.LOGWARNING)


def _hidden_hashes():
    base = _top_url()
    if not base:
        return set()
    cache = USER_DATA_FOLDER + 'dead_cache.json'

    def _read_cache():
        try:
            with open(cache, 'r', encoding='utf-8') as f:
                rows = json.load(f)
            return rows if isinstance(rows, list) else []
        except Exception:
            return None

    def _write_cache(rows):
        try:
            os.makedirs(USER_DATA_FOLDER, exist_ok=True)
            with open(cache, 'w', encoding='utf-8') as f:
                json.dump(rows, f)
        except Exception:
            pass

    if os.path.exists(cache) and time.time() - os.path.getmtime(cache) < TOP_CACHE_TTL:
        rows = _read_cache()
        if rows is not None:
            return set(rows)
    try:
        import requests
        r = requests.get(base, params={'action': 'dead'},
                         headers={'User-Agent': 'Kodi-poslouchej.radia'}, timeout=4)
        r.raise_for_status()
        txt = r.text
        rows = json.loads(txt[txt.index('['):txt.rindex(']') + 1])
        if not isinstance(rows, list):
            raise ValueError('neplatna data')
    except Exception as e:
        xbmc.log('[poslouchej.radia] nacteni skrytych stanic selhalo: {}'.format(e.__class__.__name__),
                 xbmc.LOGWARNING)
        rows = _read_cache() or []
    _write_cache(rows)
    return set(rows)


def _stations(stations):
    hidden = _hidden_hashes()
    if stations and hidden:
        stations = [st for st in stations if _hash(st['url']) not in hidden]
    if not stations:
        xbmcgui.Dialog().ok(ADDON_NAME, LANG(30029))
        xbmcplugin.endOfDirectory(HANDLE, succeeded=False)
        return
    for st in stations:
        label = st.get('title', '')
        if st.get('count'):
            label += '  ({}×)'.format(st['count'])
        li = xbmcgui.ListItem(label)
        img = st.get('img') or ADDON_ICON
        li.setArt({'thumb': img, 'icon': img, 'fanart': ADDON_FANART})
        li.setProperty('IsPlayable', 'true')
        url = _url('play_station',
                   name_station=str(st['title']),
                   url_station=str(st['url']),
                   img_station=str(img))
        li.addContextMenuItems([(
            LANG(30026),
            'RunPlugin(%s)' % _url('fav_add',
                                   name_station=str(st['title']),
                                   url_station=str(st['url']),
                                   img_station=str(img)))])
        xbmcplugin.addDirectoryItem(HANDLE, url, li, isFolder=False)
    xbmcplugin.endOfDirectory(HANDLE)


def show_root_menu():
    _add_dir(LANG(30607), _url('search'), _media('menu_search.png'))
    _add_dir(LANG(30003), _url('show_fav_menu'), _media('menu_favourites.png'))
    _add_dir(LANG(30004), _url('show_newest_stations'), _media('menu_new.png'))
    _add_dir(LANG(30001), _url('show_states_menu'), _media('menu_radio_tall.png'))
    _add_dir(LANG(30002), _url('show_genres_menu'), _media('menu_genres.png'))
    xbmcplugin.endOfDirectory(HANDLE)


def _visible(key):
    return ADDON.getSetting('vis_' + key.replace('-', '_')) != 'false'


def _add_cat(key, label_id, route):
    if _visible(key):
        _add_dir(LANG(label_id), _url(route))


def show_states_menu():
    _add_cat('country-sk', 30005, 'show_sk_stations')
    _add_cat('country-cz', 30006, 'show_cz_stations')
    _add_cat('country-uk', 30007, 'show_gb_stations')
    _add_cat('country-us', 30008, 'show_usa_stations')
    _add_cat('country-fr', 30009, 'show_fra_stations')
    _add_cat('country-ned', 30010, 'show_ned_stations')
    _add_cat('country-ger', 30011, 'show_ger_stations')
    _add_cat('country-pol', 30012, 'show_pol_stations')
    _add_cat('country-au', 30013, 'show_au_stations')
    _add_cat('country-ru', 30014, 'show_rus_stations')
    _add_cat('country-slo', 30035, 'show_slo_stations')
    xbmcplugin.endOfDirectory(HANDLE)


def show_genres_menu():
    _add_cat('style-dance', 30015, 'show_dance_stations')
    _add_cat('style-folk', 30016, 'show_folk_stations')
    _add_cat('style-jazz', 30017, 'show_jazz_stations')
    _add_cat('style-talk', 30018, 'show_word_stations')
    _add_cat('style-oldies', 30019, 'show_oldies_stations')
    _add_cat('style-80er', 30038, 'show_80er_stations')
    _add_cat('style-90er', 30036, 'show_90er_stations')
    _add_cat('style-00er', 30037, 'show_00er_stations')
    _add_cat('style-pop', 30020, 'show_pop_stations')
    _add_cat('style-relax', 30021, 'show_relax_stations')
    _add_cat('style-rnb', 30022, 'show_rnb_stations')
    _add_cat('style-rock', 30023, 'show_rock_stations')
    _add_cat('style-solo', 30024, 'show_solo_stations')
    _add_cat('style-news', 30025, 'show_news_stations')
    xbmcplugin.endOfDirectory(HANDLE)


def show_fav_menu():
    _add_dir(LANG(30028), _url('show_my_fav_stations'))
    _add_dir(LANG(30608), _url('show_top_listened'))
    _add_dir(LANG(30030),  _url('custom_my_station'))
    xbmcplugin.endOfDirectory(HANDLE)


def show_my_fav_stations():
    data = _load_fav()
    for el in data['stanice']:
        li = xbmcgui.ListItem(el['nazov'])
        img = el.get('img') or ADDON_ICON
        li.setArt({'thumb': img, 'icon': img, 'fanart': ADDON_FANART})
        li.setProperty('IsPlayable', 'true')
        ctx = [(LANG(30027),
                'RunPlugin(%s)' % _url('fav_remove', station_name=el['nazov']))]
        if el.get('is_custom') == '1':
            ctx.append((LANG(30034),
                        'RunPlugin(%s)' % _url('custom_edit_station', station_name=el['nazov'])))
        li.addContextMenuItems(ctx)
        xbmcplugin.addDirectoryItem(HANDLE, el['url'], li, isFolder=False)
    xbmcplugin.endOfDirectory(HANDLE)


def _ask_station(station):
    for param, lid in zip(['nazov', 'url', 'img'], [30604, 30605, 30606]):
        kb = xbmc.Keyboard(station.get(param, ''), LANG(30603) + LANG(lid))
        kb.doModal()
        station[param] = kb.getText() if kb.isConfirmed() else ''
    station['is_custom'] = '1'
    return station


def custom_my_station():
    data = _load_fav()
    station = _ask_station({})
    if not station['nazov'] or not station['url']:
        xbmcgui.Dialog().notification(LANG(30032), LANG(30031))
    else:
        data['stanice'].append(station)
        _save_fav(data)
        xbmcgui.Dialog().notification(LANG(30033), "Stanica: '{}'".format(station['nazov']))
    xbmcplugin.endOfDirectory(HANDLE, succeeded=False)


def custom_edit_station(station_name):
    data = _load_fav()
    station = next((x for x in data['stanice'] if x['nazov'] == station_name), None)
    if station is None:
        xbmcplugin.endOfDirectory(HANDLE, succeeded=False)
        return
    _ask_station(station)
    _save_fav(data)
    xbmcgui.Dialog().notification(LANG(30033), "Stanica: '{}'".format(station['nazov']))
    xbmc.executebuiltin('Container.Refresh')
    xbmcplugin.endOfDirectory(HANDLE, succeeded=False)


def fav_add(name_station, url_station, img_station):
    data = _load_fav()
    play_url = _url('play_station', name_station=name_station,
                    url_station=url_station, img_station=img_station)
    data['stanice'] = [e for e in data['stanice']
                       if e.get('nazov') != name_station and e.get('url') != play_url]
    data['stanice'].append({'nazov': name_station, 'url': play_url,
                            'img': img_station, 'is_custom': '0'})
    _save_fav(data)
    xbmcgui.Dialog().notification(
        ADDON_NAME, "{}: '{}'".format(LANG(30033), name_station), ADDON_ICON, 2500)


def fav_remove(station_name):
    data = _load_fav()
    data['stanice'] = [e for e in data['stanice'] if e.get('nazov') != station_name]
    _save_fav(data)
    xbmc.executebuiltin('Container.Refresh')


def search():
    kb = xbmc.Keyboard('', LANG(30604))
    kb.doModal()
    if kb.isConfirmed() and kb.getText():
        _stations(radio_api.search_stations_by_string(kb.getText()))
    else:
        xbmcplugin.endOfDirectory(HANDLE, succeeded=False)


def _verify_stream(url, name):
    if _stream_ok(url):
        return
    monitor, player = xbmc.Monitor(), xbmc.Player()
    for _ in range(10):
        try:
            if (player.isPlayingAudio()
                    and player.getPlayingFile().split('|')[0] == url):
                return
        except RuntimeError:
            pass
        if monitor.waitForAbort(1):
            return
    xbmc.log('[poslouchej.radia] Dead stream: {}'.format(url), xbmc.LOGWARNING)
    xbmcgui.Dialog().notification(
        ADDON_NAME, 'Stream neni funkcni', xbmcgui.NOTIFICATION_ERROR, 3000)
    _report_dead(url, name)


def play_station(url_station, name_station, img_station):
    li = xbmcgui.ListItem(name_station)
    li.setArt({'thumb': img_station, 'icon': img_station, 'fanart': ADDON_FANART})
    li.setPath(url_station)
    xbmcplugin.setResolvedUrl(HANDLE, True, li)
    threading.Thread(target=_verify_stream, args=(url_station, name_station),
                     daemon=True).start()
    _track_listening(url_station, name_station, img_station)


def clear_cache():
    removed = 0
    if os.path.isdir(CACHE_DIR):
        for name in os.listdir(CACHE_DIR):
            if name.endswith('.json') or name.endswith('.tmp'):
                try:
                    os.remove(os.path.join(CACHE_DIR, name))
                    removed += 1
                except OSError as e:
                    xbmc.log('[poslouchej.radia] nelze smazat {}: {}'.format(name, e),
                             xbmc.LOGWARNING)
    _dead_hosts.clear()
    xbmc.log('[poslouchej.radia] mezipaměť vymazána ({} souborů)'.format(removed),
             xbmc.LOGINFO)
    xbmcgui.Dialog().notification(ADDON_NAME, LANG(30705), ADDON_ICON, 3000)


_ROUTES = {
    '':                    show_root_menu,
    'show_root_menu':      show_root_menu,
    'show_states_menu':    show_states_menu,
    'show_genres_menu':    show_genres_menu,
    'show_fav_menu':       show_fav_menu,
    'show_newest_stations':  lambda: _stations(radio_api.get_newest_stations()),
    'show_sk_stations':      lambda: _stations(radio_api.get_sk_stations()),
    'show_cz_stations':      lambda: _stations(radio_api.get_cz_stations()),
    'show_gb_stations':      lambda: _stations(radio_api.get_gb_stations()),
    'show_usa_stations':     lambda: _stations(radio_api.get_usa_stations()),
    'show_fra_stations':     lambda: _stations(radio_api.get_fra_stations()),
    'show_ned_stations':     lambda: _stations(radio_api.get_ned_stations()),
    'show_ger_stations':     lambda: _stations(radio_api.get_ger_stations()),
    'show_pol_stations':     lambda: _stations(radio_api.get_pol_stations()),
    'show_au_stations':      lambda: _stations(radio_api.get_au_stations()),
    'show_rus_stations':     lambda: _stations(radio_api.get_rus_stations()),
    'show_slo_stations':     lambda: _stations(radio_api.get_slo_stations()),
    'show_dance_stations':   lambda: _stations(radio_api.get_dance_stations()),
    'show_folk_stations':    lambda: _stations(radio_api.get_folk_stations()),
    'show_jazz_stations':    lambda: _stations(radio_api.get_jazz_stations()),
    'show_word_stations':    lambda: _stations(radio_api.get_word_stations()),
    'show_oldies_stations':  lambda: _stations(radio_api.get_oldies_stations()),
    'show_80er_stations':    lambda: _stations(radio_api.get_80er_stations()),
    'show_90er_stations':    lambda: _stations(radio_api.get_90er_stations()),
    'show_00er_stations':    lambda: _stations(radio_api.get_00er_stations()),
    'show_pop_stations':     lambda: _stations(radio_api.get_pop_stations()),
    'show_relax_stations':   lambda: _stations(radio_api.get_relax_stations()),
    'show_rnb_stations':     lambda: _stations(radio_api.get_rnb_stations()),
    'show_rock_stations':    lambda: _stations(radio_api.get_rock_stations()),
    'show_solo_stations':    lambda: _stations(radio_api.get_solo_stations()),
    'show_news_stations':    lambda: _stations(radio_api.get_news_stations()),
    'show_topsk_stations':   lambda: _stations(radio_api.get_topsk_stations()),
    'show_topcz_stations':   lambda: _stations(radio_api.get_topcz_stations()),
    'show_my_fav_stations':  show_my_fav_stations,
    'custom_my_station':     custom_my_station,
    'show_top_listened':     show_top_listened,
    'search':                search,
    'clear_cache':           clear_cache,
}


def run():
    _apply_advancedsettings()
    params = dict(urllib.parse.parse_qsl(sys.argv[2][1:]))
    route  = params.get('route', '')

    if route == 'play_station':
        play_station(
            url_station=params.get('url_station', ''),
            name_station=params.get('name_station', ''),
            img_station=params.get('img_station', ''),
        )
    elif route == 'fav_add':
        fav_add(params.get('name_station', ''), params.get('url_station', ''),
                params.get('img_station', ''))
    elif route == 'fav_remove':
        fav_remove(params.get('station_name', ''))
    elif route == 'custom_edit_station':
        custom_edit_station(params.get('station_name', ''))
    elif route in _ROUTES:
        _ROUTES[route]()
    else:
        show_root_menu()
