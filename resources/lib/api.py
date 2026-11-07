"""
 *  Copyright (C) 2026
 *  This file is part of plugin.audio.poslouchej.radia
 *
 *  SPDX-License-Identifier: GPL-2.0-only
 *  See LICENSE.txt for more information.


"""

import base64
import hashlib
import json
import os
import re
import time
import unicodedata

import xbmc
import xbmcaddon
import xbmcvfs

ADDON = xbmcaddon.Addon(id='plugin.audio.poslouchej.radia')
BUNDLED_DIR = os.path.join(
    xbmcvfs.translatePath(ADDON.getAddonInfo('path')),
    'resources', 'data', 'stations')
USER_DIR = xbmcvfs.translatePath(
    'special://profile/addon_data/plugin.audio.poslouchej.radia/')
CACHE_DIR = os.path.join(USER_DIR, 'stations')

DEFAULT_URL = 'https://raw.githubusercontent.com/Mebox/radia-data/main/stations/'
_SEED = b'poslouchej.radia/stations/v1'
_BLOB = 'aV8XEJs+snRAnkB/VK8Z9vOLirT5Ak2rc4cDQcCgJNocO2FmQQY/lwKesFNyvdJ5WBqvUgvccDK/nZO7TV9hYECmWxv1T97by+/x1kGqDLtaD5gSMC52YS/Bw3Yp'


def _keystream(n):
    out, i = b'', 0
    while len(out) < n:
        out += hashlib.sha256(_SEED + i.to_bytes(4, 'big')).digest()
        i += 1
    return out[:n]


def _embedded_token():
    try:
        raw = base64.b64decode(_BLOB)
        return bytes(a ^ b for a, b in zip(raw, _keystream(len(raw)))).decode('ascii')
    except Exception:
        return ''


def _log(msg):
    xbmc.log('[poslouchej.radia] ' + msg, xbmc.LOGINFO)


def _norm(s):
    s = unicodedata.normalize('NFD', s or '')
    return ''.join(c for c in s if not unicodedata.combining(c)).lower()


def _read(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError('soubor musí obsahovat seznam stanic')
    return data


KEYS = [
    'country-cz', 'country-sk', 'country-uk', 'country-us', 'country-fr',
    'country-ned', 'country-ger', 'country-pol', 'country-au', 'country-ru',
    'country-slo',
    'style-dance', 'style-folk', 'style-jazz', 'style-talk', 'style-oldies',
    'style-80er', 'style-90er', 'style-00er', 'style-pop', 'style-relax', 'style-rnb', 'style-rock', 'style-solo',
    'style-news',
    'top-cz', 'top-sk', 'recent',
]
NO_SEARCH = ('top-cz', 'top-sk', 'recent')


class RadioApi:

    def __init__(self):
        self._mem = {}

    def _remote_update(self, key):
        base = (ADDON.getSetting('data_url') or '').strip() or DEFAULT_URL
        if not base.endswith('/'):
            base += '/'
        cache = os.path.join(CACHE_DIR, key + '.json')
        try:
            hours = int(ADDON.getSetting('update_hours') or 1)
        except ValueError:
            hours = 1
        if os.path.exists(cache) and time.time() - os.path.getmtime(cache) < hours * 3600:
            return
        url = base + key + '.json'
        token = (ADDON.getSetting('data_token') or '').strip() or _embedded_token()
        attempts = [(url, {})]
        m = re.match(r'https://raw\.githubusercontent\.com/([^/]+)/([^/]+)/([^/]+)/(.+)$', url)
        if m and token:
            attempts.append((
                'https://api.github.com/repos/{}/{}/contents/{}?ref={}'.format(
                    m.group(1), m.group(2), m.group(4), m.group(3)),
                {'Accept': 'application/vnd.github.raw'}))
        try:
            import requests
        except Exception as e:
            _log('requests nedostupné: {}'.format(e))
            return
        for target, extra in attempts:
            try:
                headers = {'User-Agent': 'Kodi-poslouchej.radia'}
                headers.update(extra)
                if token and re.match(r'https://(raw\.githubusercontent\.com|api\.github\.com)/', target):
                    headers['Authorization'] = 'Bearer ' + token
                r = requests.get(target, headers=headers, timeout=8)
                r.raise_for_status()
                data = json.loads(r.content.decode('utf-8'))
                if not isinstance(data, list):
                    raise ValueError('neplatná data')
                os.makedirs(CACHE_DIR, exist_ok=True)
                tmp = cache + '.tmp'
                with open(tmp, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False)
                os.replace(tmp, cache)
                _log('{}.json aktualizován'.format(key))
                return
            except Exception as e:
                _log('aktualizace {}.json selhala ({}): {}'.format(
                    key, target.split('?')[0], e.__class__.__name__))

    def _local(self, key):
        for folder in (CACHE_DIR, BUNDLED_DIR):
            path = os.path.join(folder, key + '.json')
            try:
                if os.path.exists(path):
                    return _read(path)
            except Exception as e:
                _log('nelze číst {}: {}'.format(path, e))
        return []

    def _get(self, key, refresh=True):
        if key not in self._mem:
            if refresh:
                self._remote_update(key)
            self._mem[key] = self._local(key)
        return self._mem[key] or None

    def get_sk_stations(self):      return self._get('country-sk')
    def get_cz_stations(self):      return self._get('country-cz')
    def get_gb_stations(self):      return self._get('country-uk')
    def get_usa_stations(self):     return self._get('country-us')
    def get_fra_stations(self):     return self._get('country-fr')
    def get_ned_stations(self):     return self._get('country-ned')
    def get_ger_stations(self):     return self._get('country-ger')
    def get_pol_stations(self):     return self._get('country-pol')
    def get_au_stations(self):      return self._get('country-au')
    def get_rus_stations(self):     return self._get('country-ru')
    def get_slo_stations(self):     return self._get('country-slo')

    def get_topsk_stations(self):   return self._get('top-sk')
    def get_topcz_stations(self):   return self._get('top-cz')
    def get_newest_stations(self):  return self._get('recent')

    def get_dance_stations(self):   return self._get('style-dance')
    def get_folk_stations(self):    return self._get('style-folk')
    def get_jazz_stations(self):    return self._get('style-jazz')
    def get_word_stations(self):    return self._get('style-talk')
    def get_oldies_stations(self):  return self._get('style-oldies')
    def get_80er_stations(self):    return self._get('style-80er')
    def get_90er_stations(self):    return self._get('style-90er')
    def get_00er_stations(self):    return self._get('style-00er')
    def get_pop_stations(self):     return self._get('style-pop')
    def get_relax_stations(self):   return self._get('style-relax')
    def get_rnb_stations(self):     return self._get('style-rnb')
    def get_rock_stations(self):    return self._get('style-rock')
    def get_solo_stations(self):    return self._get('style-solo')
    def get_news_stations(self):    return self._get('style-news')

    def search_stations_by_string(self, search_string):
        needle = _norm(search_string)
        if not needle:
            return None
        found, seen = [], set()
        for key in KEYS:
            if key in NO_SEARCH or ADDON.getSetting('vis_' + key.replace('-', '_')) == 'false':
                continue
            for st in self._get(key) or []:
                if st['url'] in seen:
                    continue
                if needle in _norm(st.get('title', '')):
                    seen.add(st['url'])
                    found.append(st)
        found.sort(key=lambda s: _norm(s['title']))
        return found or None
