#!/usr/bin/env python
"""
 *  Copyright (C) 2021 Mario Babinec (mr.babinec@gmail.com)
 *  This file is part of plugin.audio.poslouchej.radia
 *
 *  SPDX-License-Identifier: GPL-2.0-only
 *  See LICENSE.txt for more information.
"""
from xbmcswift2 import Plugin, xbmc, listitem
from resources.lib.api import RadioApi
import xbmcgui
import xbmcaddon
import os
import json
import xbmc

__addon__ = xbmcaddon.Addon(id='plugin.audio.poslouchej.radia')
__addonname__ = __addon__.getAddonInfo('name')
__lang__ = __addon__.getLocalizedString
__userDataFolder__ = xbmc.translatePath("special://profile/addon_data/plugin.audio.poslouchej.radia/")

plugin = Plugin()
radio_api = RadioApi()


@plugin.route('/')
def show_root_menu():
    items = (
        {'label': __addon__.getLocalizedString(30001), 'icon': plugin.icon,
         'fanart': __get_plugin_fanart(),
         'path': plugin.url_for('show_states_menu'),
         },
        {'label': __addon__.getLocalizedString(30002), 'icon': plugin.icon,
         'fanart': __get_plugin_fanart(),
         'path': plugin.url_for('show_genres_menu'),
         },
        {'label': __addon__.getLocalizedString(30003), 'icon': plugin.icon,
         'fanart': __get_plugin_fanart(),
         'path': plugin.url_for('show_fav_menu'),
         },
        {'label': __addon__.getLocalizedString(30004), 'icon': plugin.icon,
         'fanart': __get_plugin_fanart(),
         'path': plugin.url_for('show_newest_stations'),
         },
        {'label': __addon__.getLocalizedString(30607), 'icon': plugin.icon,
         'fanart': __get_plugin_fanart(),
         'path': plugin.url_for('search'),
         },
    )
    return plugin.finish(items)


# sub_menu STATES

@plugin.route('/states')
def show_states_menu():
    items = (
        {'label': __addon__.getLocalizedString(30005), 'icon': plugin.icon,
         'fanart': __get_plugin_fanart(),
         'path': plugin.url_for('show_sk_stations'),
         },
        {'label': __addon__.getLocalizedString(30006), 'icon': plugin.icon,
         'fanart': __get_plugin_fanart(),
         'path': plugin.url_for('show_cz_stations'),
         },
        {'label': __addon__.getLocalizedString(30007), 'icon': plugin.icon,
         'fanart': __get_plugin_fanart(),
         'path': plugin.url_for('show_gb_stations'),
         },
        {'label': __addon__.getLocalizedString(30008), 'icon': plugin.icon,
         'fanart': __get_plugin_fanart(),
         'path': plugin.url_for('show_usa_stations'),
         },
        {'label': __addon__.getLocalizedString(30009), 'icon': plugin.icon,
         'fanart': __get_plugin_fanart(),
         'path': plugin.url_for('show_fra_stations'),
         },
        {'label': __addon__.getLocalizedString(30010), 'icon': plugin.icon,
         'fanart': __get_plugin_fanart(),
         'path': plugin.url_for('show_ned_stations'),
         },
        {'label': __addon__.getLocalizedString(30011), 'icon': plugin.icon,
         'fanart': __get_plugin_fanart(),
         'path': plugin.url_for('show_ger_stations'),
         },
        {'label': __addon__.getLocalizedString(30012), 'icon': plugin.icon,
         'fanart': __get_plugin_fanart(),
         'path': plugin.url_for('show_pol_stations'),
         },
        {'label': __addon__.getLocalizedString(30013), 'icon': plugin.icon,
         'fanart': __get_plugin_fanart(),
         'path': plugin.url_for('show_au_stations'),
         },
        {'label': __addon__.getLocalizedString(30014), 'icon': plugin.icon,
         'fanart': __get_plugin_fanart(),
         'path': plugin.url_for('show_rus_stations'),
         },
         {'label': __addon__.getLocalizedString(30035), 'icon': plugin.icon,
          'fanart': __get_plugin_fanart(),
          'path': plugin.url_for('show_slo_stations'),
          },
    )
    return plugin.finish(items)


# sub_menu GENRES


@plugin.route('/genres')
def show_genres_menu():
    items = (
        {'label': __addon__.getLocalizedString(30015), 'icon': plugin.icon,
         'fanart': __get_plugin_fanart(),
         'path': plugin.url_for('show_dance_stations'),
         },
        {'label': __addon__.getLocalizedString(30016), 'icon': plugin.icon,
         'fanart': __get_plugin_fanart(),
         'path': plugin.url_for('show_folk_stations'),
         },
        {'label': __addon__.getLocalizedString(30017), 'icon': plugin.icon,
         'fanart': __get_plugin_fanart(),
         'path': plugin.url_for('show_jazz_stations'),
         },
        {'label': __addon__.getLocalizedString(30018), 'icon': plugin.icon,
         'fanart': __get_plugin_fanart(),
         'path': plugin.url_for('show_word_stations'),
         },
        {'label': __addon__.getLocalizedString(30019), 'icon': plugin.icon,
         'fanart': __get_plugin_fanart(),
         'path': plugin.url_for('show_oldies_stations'),
         },
        {'label': __addon__.getLocalizedString(30020), 'icon': plugin.icon,
         'fanart': __get_plugin_fanart(),
         'path': plugin.url_for('show_pop_stations'),
         },
        {'label': __addon__.getLocalizedString(30021), 'icon': plugin.icon,
         'fanart': __get_plugin_fanart(),
         'path': plugin.url_for('show_relax_stations'),
         },
        {'label': __addon__.getLocalizedString(30022), 'icon': plugin.icon,
         'fanart': __get_plugin_fanart(),
         'path': plugin.url_for('show_rnb_stations'),
         },
        {'label': __addon__.getLocalizedString(30023), 'icon': plugin.icon,
         'fanart': __get_plugin_fanart(),
         'path': plugin.url_for('show_rock_stations'),
         },
        {'label': __addon__.getLocalizedString(30024), 'icon': plugin.icon,
         'fanart': __get_plugin_fanart(),
         'path': plugin.url_for('show_solo_stations'),
         },
        {'label': __addon__.getLocalizedString(30025), 'icon': plugin.icon,
         'fanart': __get_plugin_fanart(),
         'path': plugin.url_for('show_news_stations'),
         },
    )
    return plugin.finish(items)


@plugin.route('/fav')
def show_fav_menu():
    items = (
        {'label': __addon__.getLocalizedString(30028), 'icon': plugin.icon,
         'fanart': __get_plugin_fanart(),
         'path': plugin.url_for('show_my_fav_stations'),
         },
        {'label': 'TOP 10 SK', 'icon': plugin.icon,
         'fanart': __get_plugin_fanart(),
         'path': plugin.url_for('show_topsk_stations'),
         },
        {'label': 'TOP 10 CZ', 'icon': plugin.icon,
         'fanart': __get_plugin_fanart(),
         'path': plugin.url_for('show_topcz_stations'),
         },
        {'label': __addon__.getLocalizedString(30030), 'icon': plugin.icon,
         'fanart': __get_plugin_fanart(),
         'path': plugin.url_for('custom_my_station'),
         },
    )
    return plugin.finish(items)


@plugin.route('/stations/my/custom')
def custom_my_station():
    if not os.path.exists(__userDataFolder__ + 'myFav.json'):
        open(__userDataFolder__ + 'myFav.json', 'w').write('{"stanice": []}')

    with open(__userDataFolder__ + 'myFav.json') as data_file:
        old_data = json.load(data_file)

    station = {}

    i = 0
    strings = [__addon__.getLocalizedString(30604), __addon__.getLocalizedString(30605), __addon__.getLocalizedString(
        30606)]
    h = ['nazov', 'url', 'img']
    for param in h:
        heading = __addon__.getLocalizedString(30603) + strings[i]
        station[param] = plugin.keyboard(station.get(param, ''), heading) or ''
        i = i + 1
    station['is_custom'] = '1'
    old_data['stanice'].append(station)
    if station['nazov'] == '':
        message = __addon__.getLocalizedString(30031)
        xbmcgui.Dialog().notification(__addon__.getLocalizedString(30032), message)
    else:
        with open(__userDataFolder__ + 'myFav.json', 'w+') as outfile:
            json.dump(old_data, outfile)
        message = "Stanica: '{}'".format(station['nazov'])
        xbmcgui.Dialog().notification(__addon__.getLocalizedString(30033), message)

# edit my station


@plugin.route('/stations/my/edit/<station_name>')
def custom_edit_station(station_name):
    with open(__userDataFolder__ + 'myFav.json') as data_file:
        old_data = json.load(data_file)
    data = old_data['stanice']

    station = next(item for item in data if item["nazov"] == station_name)

    i = 0
    strings = [__addon__.getLocalizedString(30604), __addon__.getLocalizedString(30605), __addon__.getLocalizedString(
        30606)]
    h = ['nazov', 'url', 'img']
    for param in h:
        heading = __addon__.getLocalizedString(30603) + strings[i]
        station[param] = plugin.keyboard(station.get(param, ''), heading) or ''
        i = i + 1
    station['is_custom'] = '1'

    with open(__userDataFolder__ + 'myFav.json', 'w+') as outfile:
        json.dump(old_data, outfile)

    message = "Stanica: '{}'".format(station['nazov'])
    xbmcgui.Dialog().notification(__addon__.getLocalizedString(30033), message)
    xbmc.executebuiltin('Container.Refresh')


#search
@plugin.route('/stations/search/')
def search():
    query = plugin.keyboard(heading=__addon__.getLocalizedString(30604))
    if query:
        url = plugin.url_for('search_result', search_string=query)
        plugin.redirect(url)


@plugin.route('/stations/search/<search_string>')
def search_result(search_string):
    stations = radio_api.search_stations_by_string(search_string)
    if not stations:
        dialog = xbmcgui.Dialog()
        dialog.ok(__addonname__, __addon__.getLocalizedString(30029))
    else:
        return __add_stations(stations)

# get states stations


@plugin.route('/stations/sk')
def show_sk_stations():
    stations = radio_api.get_sk_stations()
    if not stations:
        dialog = xbmcgui.Dialog()
        dialog.ok(__addonname__, __addon__.getLocalizedString(30029))
    else:
        return __add_stations(stations)


@plugin.route('/stations/cz')
def show_cz_stations():
    stations = radio_api.get_cz_stations()
    if not stations:
        dialog = xbmcgui.Dialog()
        dialog.ok(__addonname__, __addon__.getLocalizedString(30029))
    else:
        return __add_stations(stations)


@plugin.route('/stations/gb')
def show_gb_stations():
    stations = radio_api.get_gb_stations()
    if not stations:
        dialog = xbmcgui.Dialog()
        dialog.ok(__addonname__, __addon__.getLocalizedString(30029))
    else:
        return __add_stations(stations)


@plugin.route('/stations/usa')
def show_usa_stations():
    stations = radio_api.get_usa_stations()
    if not stations:
        dialog = xbmcgui.Dialog()
        dialog.ok(__addonname__, __addon__.getLocalizedString(30029))
    else:
        return __add_stations(stations)


@plugin.route('/stations/fra')
def show_fra_stations():
    stations = radio_api.get_fra_stations()
    if not stations:
        dialog = xbmcgui.Dialog()
        dialog.ok(__addonname__, __addon__.getLocalizedString(30029))
    else:
        return __add_stations(stations)


@plugin.route('/stations/ned')
def show_ned_stations():
    stations = radio_api.get_ned_stations()
    if not stations:
        dialog = xbmcgui.Dialog()
        dialog.ok(__addonname__, __addon__.getLocalizedString(30029))
    else:
        return __add_stations(stations)


@plugin.route('/stations/ger')
def show_ger_stations():
    stations = radio_api.get_ger_stations()
    if not stations:
        dialog = xbmcgui.Dialog()
        dialog.ok(__addonname__, __addon__.getLocalizedString(30029))
    else:
        return __add_stations(stations)


@plugin.route('/stations/pol')
def show_pol_stations():
    stations = radio_api.get_pol_stations()
    if not stations:
        dialog = xbmcgui.Dialog()
        dialog.ok(__addonname__, __addon__.getLocalizedString(30029))
    else:
        return __add_stations(stations)


@plugin.route('/stations/au')
def show_au_stations():
    stations = radio_api.get_au_stations()
    if not stations:
        dialog = xbmcgui.Dialog()
        dialog.ok(__addonname__, __addon__.getLocalizedString(30029))
    else:
        return __add_stations(stations)


@plugin.route('/stations/rus')
def show_rus_stations():
    stations = radio_api.get_rus_stations()
    if not stations:
        dialog = xbmcgui.Dialog()
        dialog.ok(__addonname__, __addon__.getLocalizedString(30029))
    else:
        return __add_stations(stations)


@plugin.route('/stations/slo')
def show_slo_stations():
    stations = radio_api.get_slo_stations()
    if not stations:
        dialog = xbmcgui.Dialog()
        dialog.ok(__addonname__, __addon__.getLocalizedString(30029))
    else:
        return __add_stations(stations)


# get Genres


@plugin.route('/stations/dance')
def show_dance_stations():
    stations = radio_api.get_dance_stations()
    if not stations:
        dialog = xbmcgui.Dialog()
        dialog.ok(__addonname__, __addon__.getLocalizedString(30029))
    else:
        return __add_stations(stations)


@plugin.route('/stations/folk')
def show_folk_stations():
    stations = radio_api.get_folk_stations()
    if not stations:
        dialog = xbmcgui.Dialog()
        dialog.ok(__addonname__, __addon__.getLocalizedString(30029))
    else:
        return __add_stations(stations)


@plugin.route('/stations/jazz')
def show_jazz_stations():
    stations = radio_api.get_jazz_stations()
    if not stations:
        dialog = xbmcgui.Dialog()
        dialog.ok(__addonname__, __addon__.getLocalizedString(30029))
    else:
        return __add_stations(stations)


@plugin.route('/stations/word')
def show_word_stations():
    stations = radio_api.get_word_stations()
    if not stations:
        dialog = xbmcgui.Dialog()
        dialog.ok(__addonname__, __addon__.getLocalizedString(30029))
    else:
        return __add_stations(stations)


@plugin.route('/stations/oldies')
def show_oldies_stations():
    stations = radio_api.get_oldies_stations()
    if not stations:
        dialog = xbmcgui.Dialog()
        dialog.ok(__addonname__, __addon__.getLocalizedString(30029))
    else:
        return __add_stations(stations)


@plugin.route('/stations/pop')
def show_pop_stations():
    stations = radio_api.get_pop_stations()
    if not stations:
        dialog = xbmcgui.Dialog()
        dialog.ok(__addonname__, __addon__.getLocalizedString(30029))
    else:
        return __add_stations(stations)


@plugin.route('/stations/relax')
def show_relax_stations():
    stations = radio_api.get_relax_stations()
    if not stations:
        dialog = xbmcgui.Dialog()
        dialog.ok(__addonname__, __addon__.getLocalizedString(30029))
    else:
        return __add_stations(stations)


@plugin.route('/stations/rnb')
def show_rnb_stations():
    stations = radio_api.get_rnb_stations()
    if not stations:
        dialog = xbmcgui.Dialog()
        dialog.ok(__addonname__, __addon__.getLocalizedString(30029))
    else:
        return __add_stations(stations)


@plugin.route('/stations/rock')
def show_rock_stations():
    stations = radio_api.get_rock_stations()
    if not stations:
        dialog = xbmcgui.Dialog()
        dialog.ok(__addonname__, __addon__.getLocalizedString(30029))
    else:
        return __add_stations(stations)


@plugin.route('/stations/solo')
def show_solo_stations():
    stations = radio_api.get_solo_stations()
    if not stations:
        dialog = xbmcgui.Dialog()
        dialog.ok(__addonname__, __addon__.getLocalizedString(30029))
    else:
        return __add_stations(stations)


@plugin.route('/stations/news')
def show_news_stations():
    stations = radio_api.get_news_stations()
    if not stations:
        dialog = xbmcgui.Dialog()
        dialog.ok(__addonname__, __addon__.getLocalizedString(30029))
    else:
        return __add_stations(stations)


# get Favourites

@plugin.route('/stations/show_my_fav_stations')
def show_my_fav_stations():
    if not os.path.exists(__userDataFolder__ + 'myFav.json'):
        open(__userDataFolder__ + 'myFav.json', 'w').write('{"stanice": []}')
    with open(__userDataFolder__ + 'myFav.json', 'r') as file:
        data = json.load(file)

    items = []
    for element in data['stanice']:
        context_menu = []
        if element['is_custom'] == "1":
            context_menu.append((
                __addon__.getLocalizedString(30034),
                'RunPlugin(%s)' % plugin.url_for('custom_edit_station', station_name=element['nazov']),
            ))

        items.append({
            'label': element['nazov'],
            'thumbnail': element['img'],
            'fanart': __get_plugin_fanart(),
            'icon': element['img'],
            'path': element['url'],
            'is_playable': True,
            'properties': {'IsPlaylist': 'True'},
            'context_menu': context_menu,
        })

    return plugin.finish(items)


@plugin.route('/stations/top_sk')
def show_topsk_stations():
    stations = radio_api.get_topsk_stations()
    if not stations:
        dialog = xbmcgui.Dialog()
        dialog.ok(__addonname__, __addon__.getLocalizedString(30029))
    else:
        return __add_stations(stations)


@plugin.route('/stations/top_cz')
def show_topcz_stations():
    stations = radio_api.get_topcz_stations()
    if not stations:
        dialog = xbmcgui.Dialog()
        dialog.ok(__addonname__, __addon__.getLocalizedString(30029))
    else:
        return __add_stations(stations)


@plugin.route('/stations/show_newest_stations')
def show_newest_stations():
    stations = radio_api.get_newest_stations()
    if not stations:
        dialog = xbmcgui.Dialog()
        dialog.ok(__addonname__, __addon__.getLocalizedString(30029))
    else:
        return __add_stations(stations)


@plugin.route('/station/<img_station>/<url_station>/<name_station>')
def get_stream_url(img_station, url_station, name_station):
    return plugin.set_resolved_url(
        listitem.ListItem(
            label=name_station,
            path=url_station,
            icon=img_station,
            thumbnail=img_station,
            fanart=__get_plugin_fanart()
        )
    )


def __add_stations(stations):
    items = []
    for station in stations:
        stationName = station['title'].encode('utf-8')
        stationImg = station['img'].encode('utf-8')
        stationUrl = station['url'].encode('utf-8')

        items.append({
            'label': stationName,
            'thumbnail': stationImg,
            'fanart': stationImg,
            'icon': stationImg,
            'path': plugin.url_for(
                'get_stream_url',
                name_station=stationName, url_station=stationUrl, img_station=stationImg,
            ),
            # 'path': station['url'],
            'is_playable': True,
            'properties': {'IsSpecial': 'True'},
        })

    return plugin.finish(items)


def __get_plugin_fanart():
    return plugin.fanart

def run():
    plugin.run()
