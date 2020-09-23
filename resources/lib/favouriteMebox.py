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
			['Club Rádio (CZ)', 'http://icecast2.play.cz:8000/Clubradio.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc18.jpg'],
			['Impuls Rádio (CZ)', 'http://icecast5.play.cz/impuls128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioi12.jpg'],
		        ['Rádio Blaník (CZ)', 'http://ice.abradio.cz/blanikfm128.mp3?i=86.22812972256186', 'https://i62.servimg.com/u/f62/19/40/01/67/radiob12.jpg'],
			['Rádio Kiss (CZ)', 'http://icecast4.play.cz:8000/kiss128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok13.jpg'],
			['Rádio Nostalgie (CZ)', 'http://icecast3.play.cz/radio-nostalgie128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radion13.jpg'],
			['Rádio Beta - Hity 80s a 90s (SK)', 'http://109.71.67.102:8000/beta_80a90.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/beta8010.jpg'],
			['OpenFM - Italo Disco (PL)', 'https://stream.open.fm/27', 'https://i46.servimg.com/u/f46/19/40/01/67/c17580.png'],
		        ['Radio Danz (USA)', 'http://107.182.230.133/stream?icy=http', 'https://i62.servimg.com/u/f62/19/40/01/67/radio_13.png'],
		        ['One Dance (I)', 'http://ice10.fluidstream.net/rn1_2.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175136.png'],
			['FFH Eurodance (D)', 'http://mp3.ffh.de/ffhchannels/hqeurodance.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/ffh_di11.jpg']
			            ]

        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?topmebox_' + str(i), listitem=listItem, isFolder=True)
                i = i + 1
            xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
        else:
        
            Title = list[int(self.opt2)][0]
            Icon = list[int(self.opt2)][2]
            URL = list[int(self.opt2)][1]
        
            import radioPlayer as player
            player.Main().start(Title, Icon, URL)
