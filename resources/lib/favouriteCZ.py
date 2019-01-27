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
            ['Impuls RÃ¡dio', 'http://icecast5.play.cz/impuls128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioi12.jpg'],
			['Cesky rozhlas 1 - Radiozurnal', 'http://icecast7.play.cz:443/cro1-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior12.jpg'],
			['Evropa 2', 'http://icecast3.play.cz/evropa2-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioe11.jpg'],
			['Frekvence 1', 'http://icecast4.play.cz/frekvence1-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiof16.jpg'],
			['Radio Blani­k', 'http://ice.abradio.cz/blanikfm128.mp3?i=86.22812972256186', 'https://i62.servimg.com/u/f62/19/40/01/67/radiob12.jpg'],
			['Hitradio FM', 'http://ice.abradio.cz/hitradiofm128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitrad15.jpg'],
			['Radio Kiss', 'http://icecast4.play.cz:8000/kiss128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok13.jpg'],
			['Cesky rozhlas 2 - Praha', 'http://icecast7.play.cz:443/cro2-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc22.jpg'],
			['Radio Beat', 'http://ice6.abradio.cz/beat128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/beat10.png'],
			['Radio Country', 'http://mp3stream4.abradio.cz/country128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc14.jpg'],
            ]

        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?topCZ_' + str(i), listitem=listItem, isFolder=True)
                i = i + 1
            xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
        else:
        
            Title = list[int(self.opt2)][0]
            Icon = list[int(self.opt2)][2]
            URL = list[int(self.opt2)][1]
        
            import radioPlayer as player
            player.Main().start(Title, Icon, URL)
