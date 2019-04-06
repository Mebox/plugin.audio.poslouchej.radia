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
            ['Cimrmanovo rádio (CZ)', 'http://liquiddoom.net:8000/cimrman', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc20.jpg'],
            ['Český Rozhlas Rádio Retro (CZ)', 'http://icecast7.play.cz/croretro128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior13.jpg'],
            ['Pigy.cz - Pohádky (CZ)', 'http://pool.cdn.lagardere.cz/web-pg-pohadky', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop10.jpg'],
            ['Rádio Humor (CZ)', 'http://mp3stream4.abradio.cz:8000/humor128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh13.jpg'],
            ['Rádio Pohádka  (CZ)', 'http://ice3.abradio.cz/pohadka128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop12.jpg'],
            ['Rádio Povídka (CZ)', 'http://ice.abradio.cz/povidka128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop11.jpg'],
            ['Detské rádio - Rozprávky (CZ)', 'http://stream.detskeradio.sk/rozpravky.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radioz12.jpg'],
            ['Rádio Litera (CZ)', 'http://icecast.stv.livebox.sk/litera_128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiol12.jpg']
                        ]

        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?ms_' + str(i), listitem=listItem, isFolder=True)
                i = i + 1
            xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
        else:
        
            Title = list[int(self.opt2)][0]
            Icon = list[int(self.opt2)][2]
            URL = list[int(self.opt2)][1]
        
            import radioPlayer as player
            player.Main().start(Title, Icon, URL)
            
