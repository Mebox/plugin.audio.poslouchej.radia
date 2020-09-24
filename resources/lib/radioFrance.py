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
            ['B4B Radio Club Dance', 'https://radio10.pro-fhi.net/radio/9000/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/c17559.png'],
            ['E-Dance 90s', 'http://94.23.221.158:9197/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/c17567.png'],
            ['Hit West 80s', 'https://listen.shoutcast.com/HITWEST80.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17583.png'],
            ['Hotmixradio 80', 'http://streaming.hotmixradio.fm/hotmixradio-80-128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17560.png'],
            ['Hotmixradio FUNKY', 'http://streaming.hotmixradio.fm/hotmixradio-funky-128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17563.png'],
            ['Hotmixradio LOUNGE', 'http://streaming.hotmixradio.fm/hotmixradio-lounge-128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17564.png'],
            ['Hotmixradio HITS', 'http://streaming.hotmixradio.fm/hotmixradio-hits-128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17572.png'],
            ['Hotmixradio 2000', 'http://streaming.hotmixradio.fm/hotmixradio-2k-128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17573.png'],
            ['Hotmixradio HOT', 'http://streaming.hotmixradio.fm/hotmixradio-hot-128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17574.png'],
            ['NRJ France', 'http://185.52.127.168/fr/30001/mp3_128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17570.png'],
            ['Puls Radio - Lounge', 'http://icecast.pulsradio.com/relaxHD.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/lounfe10.jpg'],
            ['Roots Legacy Radio', 'http://rootslegacy.fr:8080/stream/1/', 'https://i46.servimg.com/u/f46/19/40/01/67/c17566.png'],
            ['RTL2', 'http://streaming.radio.rtl2.fr/rtl2-1-48-192', 'https://i46.servimg.com/u/f46/19/40/01/67/c17569.png']
            ]

        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?fr_' + str(i), listitem=listItem, isFolder=True)
                i = i + 1
            xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
        else:
        
            Title = list[int(self.opt2)][0]
            Icon = list[int(self.opt2)][2]
            URL = list[int(self.opt2)][1]
        
            import radioPlayer as player
            player.Main().start(Title, Icon, URL)
            
