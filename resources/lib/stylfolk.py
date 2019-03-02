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
            ['Country Rádio (CZ)', 'http://icecast4.play.cz:443/country128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc33.jpg'],
            ['Rádio 66 (CZ)', 'http://ice3.abradio.cz/route128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radio610.jpg'],
            ['Rádio Country (CZ)', 'http://mp3stream4.abradio.cz/country128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc14.jpg'],
            ['Rádio Folk (CZ)', 'http://mp3stream2.abradio.cz/folk128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiof15.jpg'],
            ['Rádio Dálnice (CZ)', 'http://icecast8.play.cz/radiodalnice.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/radio-10.png'],
            ['Rádio Petrov Folk (CZ)', 'http://play.radiopetrov.com:8000/petrovFC', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop14.jpg'],
            ['Rádio Samson FM (CZ)', 'http://icecast8.play.cz/samsonfm128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios17.jpg'],
            ['181.fm 90s Country (USA)', 'http://uplink.duplexfx.com:8050', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm Real Country (USA)', 'http://relay.181.fm:8034', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png']
            ]

        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?fo_' + str(i), listitem=listItem, isFolder=True)
                i = i + 1
            xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
        else:
        
            Title = list[int(self.opt2)][0]
            Icon = list[int(self.opt2)][2]
            URL = list[int(self.opt2)][1]
        
            import radioPlayer as player
            player.Main().start(Title, Icon, URL)
            
