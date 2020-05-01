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
            ['101.ru: Radio 70s FM  (RU)', 'http://air2.radiorecord.ru:9002/1970_128', 'https://static.radio.net/images/broadcasts/73/8a/7121/1/c300.png'],
            ['101.ru: Radio 80s FM  (RU)', 'http://air2.radiorecord.ru:9002/1980_128', 'https://static.radio.net/images/broadcasts/73/8a/7121/1/c300.png'],
            ['101.ru: Radio Romantica FM  (RU)', 'http://ic7.101.ru:8000/v4_1', 'https://static.radio.net/images/broadcasts/73/8a/7121/1/c300.png'],
            ['101.ru: Euro Hits (RU)', 'https://ic7.101.ru:8000/c16_13', 'https://static.radio.net/images/broadcasts/73/8a/7121/1/c300.png'],
            ['16bit.FM - ProBeat', 'http://16bitfm.com:8000/main_mp3_192', 'https://i46.servimg.com/u/f46/19/40/01/67/c17538.png'],
            ['AvtoRadio', 'http://ic7.101.ru:8000/v3_1', 'https://i46.servimg.com/u/f46/19/40/01/67/c17529.png'],
            ['Best FM Moscow', 'http://nashe1.hostingradio.ru/best-128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17530.png'],
            ['Europa Plus ru', 'http://ep256.hostingradio.ru:8052/europaplus256.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17533.png'],
            ['Makradio Retro Hits', 'http://air.volna.top/makkirus128?stream=1548523420', 'https://i46.servimg.com/u/f46/19/40/01/67/c17591.png'],
            ['MAXXX Radio', 'http://46.105.180.202:8045/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/maxrad10.jpg'],
            ['Metaradio', 'http://s2.metaradio.ru/mradio.orbox2', 'https://i46.servimg.com/u/f46/19/40/01/67/c17543.png'],
            ['NRJ 104.2 FM Moscow', 'http://ic7.101.ru:8000/v1_1', 'https://i46.servimg.com/u/f46/19/40/01/67/c17537.png'],
            ['Rock FM - 80s', 'http://jfm1.hostingradio.ru:14536/rock80.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17590.png'],
            ['Rock FM - 90s', 'http://jfm1.hostingradio.ru:14536/rock90.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17590.png'],
            ['Rock FM - 00s', 'http://jfm1.hostingradio.ru:14536/rock00.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17590.png'],
            ['Rock FM - Heavy', 'http://jfm1.hostingradio.ru:14536/metal.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17590.png'], 
            ['Radio Record Rock', 'http://air.radiorecord.ru:8102/rock_128', 'https://i46.servimg.com/u/f46/19/40/01/67/c17541.png'],
            ['Radio Ultra 70.19 FM', 'http://nashe1.hostingradio.ru/ultra-128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17534.png'],
            ['Radio Caprice - Progressive Metal', 'http://79.120.77.11:8000/progmetal', 'https://i46.servimg.com/u/f46/19/40/01/67/c17535.png'],
            ['Radio Caprice - AOR/Melodic Hard Rock', 'http://79.111.14.76:8000/aor', 'https://i46.servimg.com/u/f46/19/40/01/67/c17536.png'],
            ['San FM - Trance Channel', 'http://sanfm.ru:8000/trance', 'https://i46.servimg.com/u/f46/19/40/01/67/c17539.png'],
            ['Visual neoclassical Omdaru radio', 'http://s02.radio-tochka.com:5440/radio', 'https://i46.servimg.com/u/f46/19/40/01/67/c17542.png']
            ]

        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?ru_' + str(i), listitem=listItem, isFolder=True)
                i = i + 1
            xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
        else:
        
            Title = list[int(self.opt2)][0]
            Icon = list[int(self.opt2)][2]
            URL = list[int(self.opt2)][1]
        
            import radioPlayer as player
            player.Main().start(Title, Icon, URL)
    
