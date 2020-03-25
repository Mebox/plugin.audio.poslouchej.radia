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
            ['Radio Domino (CZ)', 'http://mp3stream4.abradio.cz/domino128.mp3', 'https://i.servimg.com/u/f62/19/40/01/67/radiod14.jpg'],
            ['Svobodný vysílač CS (CZ)', 'http://78.108.110.114:8000/live.opus', 'https://i46.servimg.com/u/f46/19/40/01/67/svobod11.jpg'],
            ['Radio23.cz - Techno (CZ)', 'http://r23.cz/tekno', 'https://i46.servimg.com/u/f46/19/40/01/67/radio210.jpg'],
            ['Radio23.cz - Breaks (CZ)', 'http://r23.cz/breaks', 'https://i46.servimg.com/u/f46/19/40/01/67/radio210.jpg'],
            ['Radio23.cz - Psytrance (CZ)', 'http://r23.cz/psy', 'https://i46.servimg.com/u/f46/19/40/01/67/radio210.jpg'],
            ['Radio23.cz - Dnb (CZ)', 'http://r23.cz/dnb', 'https://i46.servimg.com/u/f46/19/40/01/67/radio210.jpg'],
            ['Radio23.cz - Hardcore (CZ)', 'http://r23.cz/hc', 'https://i46.servimg.com/u/f46/19/40/01/67/radio210.jpg'],
            ['Radio23.cz - USB (CZ)', 'http://radio.unbros.cz/usb_autodj', 'https://i46.servimg.com/u/f46/19/40/01/67/radio210.jpg'],
            ['Radio Svit (CZ)', 'http://78.24.9.110:9490', 'https://i.servimg.com/u/f46/19/40/01/67/svit10.jpg'],
            ['Radio Karoline (CZ)', 'https://node-23.zeno.fm/hcnnke8pxneuv?rj-ttl=5&rj-tok=AAABcQyk9gcAgy7Irc2Hk6uEdg', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_23.jpg'],
            ['Funkstar Radio (CZ)', 'http://167.114.64.181:8698/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/funkst10.jpg'],
            ['Blues Sky (CZ)', 'https://node-05.zeno.fm/0hx4b9zscseuv?rj-ttl=5&rj-tok=AAABcQzR__wA_g1Ji3kf17PHog', 'https://i46.servimg.com/u/f46/19/40/01/67/blues_10.jpg'],
            ['Radio Vambi (CZ)', 'https://node-15.zeno.fm/avzpd35rckeuv?rj-ttl=5&rj-tok=AAABcQzVTcMAWSQJ94pqkxNnqg', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_24.jpg'],
            ['Radio O.K. (CZ) (nepravidelné vysílání)', 'https://node-10.zeno.fm/q7ura4u1akeuv?rj-ttl=5&rj-tok=AAABcQzZKFEAVyDUuNyclleYsg', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_25.jpg'],
            ['Rádio Stella (CZ)', 'https://ice3.abradio.cz/stella128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/rdio_s11.jpg'],
            ['Radio Like (CZ)', 'https://node-30.zeno.fm/qffde4ffzmzuv?rj-ttl=5&rj-tok=AAABcQ0Vds0A0bakXrycnR4LTA', 'https://i.servimg.com/u/f46/19/40/01/67/radio_27.jpg'],
            ['Radio Cesky Jukebox (CZ)', 'http://sc.ipip.cz:8046', 'https://i46.servimg.com/u/f46/19/40/01/67/radio-10.jpg'],
            ['West Radio (CZ)', 'https://node-16.zeno.fm/y6gyh7gg6heuv?rj-ttl=5&rj-tok=AAABcQ1G1YUAMgmz_r2kci4pLg', 'https://i46.servimg.com/u/f46/19/40/01/67/west-r10.jpg'],
            ['Radio SoundWave (CZ)', 'http://81.91.84.138:8040', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_29.jpg'],
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
            ['101.ru: Radio 70s FM  (RU)', 'http://air2.radiorecord.ru:9002/1970_128', 'https://static.radio.net/images/broadcasts/73/8a/7121/1/c300.png'],
            ['101.ru: Radio 80s FM  (RU)', 'http://air2.radiorecord.ru:9002/1980_128', 'https://static.radio.net/images/broadcasts/73/8a/7121/1/c300.png'],
            ['101.ru: Radio Romantica FM  (RU)', 'http://ic7.101.ru:8000/v4_1', 'https://static.radio.net/images/broadcasts/73/8a/7121/1/c300.png'],
            ['101.ru: Euro Hits (RU)', 'https://ic7.101.ru:8000/c16_13', 'https://static.radio.net/images/broadcasts/73/8a/7121/1/c300.png'],
            ['OpenFM - 80s Hits (PL)', 'http://stream.polskastacja.pl/ps3_mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17532.png'],
            ['RMI - Italo Disco Greatest Hits (PL)', 'http://188.165.195.176:8046/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/c17528.png'],
            ['Mega Dance Radio (HU)', 'http://megadanceradio.hopto.org:8000/livemega.mp3?', 'https://i46.servimg.com/u/f46/19/40/01/67/mega_d10.jpg']
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
