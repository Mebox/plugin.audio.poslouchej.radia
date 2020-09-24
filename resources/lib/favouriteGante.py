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
			['Mega Dance Radio (HU)', 'http://megadanceradio.hopto.org:8000/livemega.mp3?', 'https://i46.servimg.com/u/f46/19/40/01/67/mega_d10.jpg'],
			['Eurohits 101 Hits Radio (RU)', 'http://ic7.101.ru:8000/c16_13', 'https://static.radio.net/images/broadcasts/73/8a/7121/1/c300.png'],
		        ['Záhorácké Rádio (SK)', 'http://live.zahorackeradio.sk:8000/zr128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radioz10.jpg'],
			['Disco Party Radio (D)', 'http://stream.laut.fm/-z-i-s-c-o-party-70s-80s', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_33.jpg'],
			['Radio On Disco (D)', 'https://0n-disco.radionetz.de/0n-disco.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_32.jpg'],
			['Radio 70s FM (RU)', 'http://air2.radiorecord.ru:9002/1970_128', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_35.jpg'],
			['Radio 80s FM (RU)', 'http://air2.radiorecord.ru:9002/1980_128', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_34.jpg'],
		        ['Eurodisco Hit Radio (RU)', 'http://188.165.195.176:8034/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_30.jpg'],
		        ['Radio Stad Den Haag (NL)', 'http://94.228.133.3:80/;stream.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios19.jpg'],
			['80s80s Italo Disco (D)', 'https://streams.80s80s.de/italohits/mp3-192/radiode/', 'https://i46.servimg.com/u/f46/19/40/01/67/c17585.png']
               ]
        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?topgante_' + str(i), listitem=listItem, isFolder=True)
                i = i + 1
            xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
        else:
        
            Title = list[int(self.opt2)][0]
            Icon = list[int(self.opt2)][2]
            URL = list[int(self.opt2)][1]
        
            import radioPlayer as player
            player.Main().start(Title, Icon, URL)
