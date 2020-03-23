# -*- coding: utf-8 -*-

import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import os
import sys
import re
import urllib
import urllib2
import cookielib

__addon__           = xbmcaddon.Addon()
__addon_id__        = __addon__.getAddonInfo('id')
__addonname__       = __addon__.getAddonInfo('name')
__icon__            = __addon__.getAddonInfo('icon')
__addonpath__       = xbmc.translatePath(__addon__.getAddonInfo('path'))
__lang__            = __addon__.getLocalizedString
__path__            = os.path.join(__addonpath__, 'resources', 'lib' )
__path_img__        = os.path.join(__addonpath__, 'resources', 'media' )

sys.path.append(__path__)
sys.path.append (__path_img__)

class Main:

    def start(self, selfGet):

        # vars
        self = selfGet

        list = [
            ['Rádio Pelhřimov (CZ) (zkušební vysílání)', 'http://ca9.rcast.net:8054/', 'https://i.servimg.com/u/f46/19/40/01/67/rdio_p10.jpg'],
            ['Rádio Západ (CZ)', 'http://icecast9.play.cz/radio-zapad-128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/zapad10.jpg'],
            ['M1.FM - Kuschelschlager (D)', 'http://tuner.m1.fm/kuschelschlager.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/m1fm1810.png'],
            ['M1.FM - Charts (D)', 'http://tuner.m1.fm/charts.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/charts10.jpg'],
            ['M1.FM - Hits (D)', 'http://tuner.m1.fm/hits.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hits-c10.jpg'],
            ['M1.FM - Clubmix (D)', 'http://tuner.m1.fm/clubmix.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/clubmi10.jpg'],
            ['M1.FM - Softpop (D)', 'http://tuner.m1.fm/softpop.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/softpo10.jpg'],
            ['M1.FM - Chillout (D)', 'http://tuner.m1.fm/chillout.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/chillo10.jpg'],
            ['M1.FM - Urban (D)', 'http://tuner.m1.fm/urban.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/urban-10.jpg'],
            ['M1.FM - Rock (D)', 'http://tuner.m1.fm/rock.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/rock-c10.jpg'],
            ['M1.FM - Schlagerparty (D)', 'http://tuner.m1.fm/schlagerparty.mp3', 'https://i.servimg.com/u/f46/19/40/01/67/schlag10.jpg'],
            ['M1.FM - Oldies (D)', 'http://tuner.m1.fm/oldies.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/oldies10.jpg'],
            ['M1.FM - 80ER (D)', 'http://tuner.m1.fm/80er.mp3', 'https://i.servimg.com/u/f46/19/40/01/67/80er-c10.jpg'],
            ['M1.FM - 90ER (D)', 'http://tuner.m1.fm/90er.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/90er-c10.jpg'],
            ['Antenne Niederrhein (D)', 'http://antennenr-ais-edge-3003.fra-eco.cdn.addradio.net/antennenr/live/mp3/high?ar-distributor=f0a0', 'https://i.servimg.com/u/f46/19/40/01/67/antenn10.jpg'],
            ['Antenne Niederrhein - Dein Urban Radio (D)', 'http://rnrw-ais-edge-4005-212-122-133-230.cast.addradio.de/rnrw-0182/deinurban/high/stream.mp3?ar-distributor=f0a0&sid=0182&kombi=FunkkombiWest&_art=dj0yJmlwPTkzLjE4NS41OC4xOCZpZD1pY3NjeGwtbmRoc2tmeGtiJnQ9MTU4NTA1NTUyNCZzPTc4NjZmMjljI2U5NDJhZDA3NTVkNzQ3Yjc5YTc3NDdmMWY3MjQxNmEx', 'https://i.servimg.com/u/f46/19/40/01/67/rnrw-u10.png'],
            ['Antenne Niederrhein - Dein 90er Radio (D)', 'http://rnrw-ais-edge-4004-212-122-133-229.cast.addradio.de/rnrw-0182/dein90er/high/stream.mp3?ar-distributor=f0a0&sid=0182&kombi=FunkkombiWest&_art=dj0yJmlwPTkzLjE4NS41OC4xOCZpZD1pY3NjeGwtNjJ4N2h0eWtiJnQ9MTU4NTA1NTE0NCZzPTc4NjZmMjljIzIzYjcxOTBmYWQwODdiNjM4NDdlZTc0MDViZmZhOWEw', 'https://i46.servimg.com/u/f46/19/40/01/67/rnrw-910.png'],
            ['Antenne Niederrhein - Dein 80er Radio (D)', 'http://rnrw-ais-edge-3001.fra-eco.cdn.addradio.net/rnrw-0182/dein80er/high/stream.mp3?ar-distributor=f0a0&sid=0182&kombi=FunkkombiWest&_art=dj0yJmlwPTkzLjE4NS41OC4xOCZpZD1pY3NjeGwtMjZnc2tmeGtiJnQ9MTU4NTA1NDgyNCZzPTc4NjZmMjljI2UzOGI3ZjlhNGY1MTVlODM2NmRkN2Y3MWUwNTdjZDBk', 'https://i46.servimg.com/u/f46/19/40/01/67/rnrw-810.png'],
            ['Antenne Niederrhein - Dein Top 40 Radio (D)', 'http://rnrw-ais-edge-3001.fra-eco.cdn.addradio.net/rnrw-0182/deintop40/high/stream.mp3?ar-distributor=f0a0&sid=0182&kombi=FunkkombiWest&_art=dj0yJmlwPTkzLjE4NS41OC4xOCZpZD1pY3NjeGwtNWhoc2tmeGtiJnQ9MTU4NTA1NTU3MCZzPTc4NjZmMjljIzM3ZjkyM2M5MzRiZGM2MTA3MWI5YWQwMDI2M2YwZGYz', 'https://i.servimg.com/u/f46/19/40/01/67/rnrw-t10.png'],
            ['Antenne Niederrhein - Dein Lounge Radio (D)', 'http://rnrw-ais-edge-3007.fra-eco.cdn.addradio.net/rnrw-0182/deinlounge/high/stream.mp3?ar-distributor=f0a0&sid=0182&kombi=FunkkombiWest&_art=dj0yJmlwPTkzLjE4NS41OC4xOCZpZD1pY3NjeGwtNHFoc2tmeGtiJnQ9MTU4NTA1NTY1MSZzPTc4NjZmMjljIzc2MjMyOWNhNDhkMDg3YmUwYjVlYjJmYjEzOTU2OWNj', 'https://i46.servimg.com/u/f46/19/40/01/67/rnrw-l10.png'],
            ['Antenne Niederrhein - Dein Deutsch Pop Radio (D)', 'http://rnrw-ais-edge-3008.fra-eco.cdn.addradio.net/rnrw-0182/deindeutschpop/high/stream.mp3?ar-distributor=f0a0&sid=0182&kombi=FunkkombiWest&_art=dj0yJmlwPTkzLjE4NS41OC4xOCZpZD1pY3NjeGwtZWp5N2h0eWtiJnQ9MTU4NTA1NTcyOCZzPTc4NjZmMjljI2ViNzBhMmFiNDNlZmU1YmM1NzdlZTY0ZWYwZmU0YzEw', 'https://i46.servimg.com/u/f46/19/40/01/67/rnrw-d10.png'],
            ['Antenne Niederrhein - Dein Schlager Radio (D)', 'http://rnrw-ais-edge-3008.fra-eco.cdn.addradio.net/rnrw-0182/deinschlager/high/stream.mp3?ar-distributor=f0a0&sid=0182&kombi=FunkkombiWest&_art=dj0yJmlwPTkzLjE4NS41OC4xOCZpZD1pY3NjeGwta2V5N2h0eWtiJnQ9MTU4NTA1ODU4MyZzPTc4NjZmMjljI2Q5ODM1N2RkZjc2ODliMjA4NmFhZWMyMDY3ZWNkMzkx', 'https://i46.servimg.com/u/f46/19/40/01/67/rnrw-s11.png'],
            ['Antenne Niederrhein - Dein Rock Radio (D)', 'http://rnrw-ais-edge-3005.fra-eco.cdn.addradio.net/rnrw-0182/deinrock/high/stream.mp3?ar-distributor=f0a0&sid=0182&kombi=FunkkombiWest&_art=dj0yJmlwPTkzLjE4NS41OC4xOCZpZD1pY3NjeGwtbW1oc2tmeGtiJnQ9MTU4NTA1ODY1MSZzPTc4NjZmMjljI2FhNmNkOTZjMjA1Y2M2ZGQwMDQ3NDMyZDcwZGRmZTNh', 'https://i46.servimg.com/u/f46/19/40/01/67/rnrw-r10.png'],
            ['101.ru: Euro Hits (RU)', 'https://ic7.101.ru:8000/c16_13', 'https://static.radio.net/images/broadcasts/73/8a/7121/1/c300.png']
            ]

        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?new_' + str(i), listitem=listItem, isFolder=True)
                i = i + 1
            xbmcplugin.endOfDirectory(int(sys.argv[1]))

        else:

            Title = list[int(self.opt2)][0]
            Icon = list[int(self.opt2)][2]
            URL = list[int(self.opt2)][1]

            import radioPlayer as player
            player.Main().start(Title, Icon, URL)
