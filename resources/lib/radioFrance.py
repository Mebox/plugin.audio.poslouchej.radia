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
            ['B4B Radio Club Dance', 'http://b4bsecours2.radioca.st/8727/', 'https://i46.servimg.com/u/f46/19/40/01/67/c17559.png'],
            ['Hotmixradio 80', 'http://streaming.hotmixradio.fm/hotmixradio-80-128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17560.png'],
            ['Hotmixradio FUNKY', 'http://streaming.hotmixradio.fm/hotmixradio-funky-128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17563.png'],
            ['Hotmixradio LOUNGE', 'http://streaming.hotmixradio.fm/hotmixradio-lounge-128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17564.png'],
            ['Hotmixradio HITS', 'http://streaming.hotmixradio.fm/hotmixradio-hits-128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17572.png'],
            ['Hotmixradio 2000', 'http://streaming.hotmixradio.fm/hotmixradio-2k-128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17573.png'],
            ['Hotmixradio HOT', 'http://streaming.hotmixradio.fm/hotmixradio-hot-128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17574.png'],
            ['NRJ France', 'http://185.52.127.155/fr/30001/mp3_128.mp3?origine=radio.net', 'https://i46.servimg.com/u/f46/19/40/01/67/c17570.png'],
            ['E-Dance 90s', 'http://94.23.221.158:9197/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/c17567.png'],
            ['RTL2', 'http://streaming.radio.rtl2.fr/rtl2-1-48-192', 'https://i46.servimg.com/u/f46/19/40/01/67/c17569.png'],
            ['Virgin Radio Officiel', 'http://mp3lg4.tdf-cdn.com/9243/lag_164753.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17571.png'],
            ['Feeling Floyd Rock', 'http://195.154.180.106:8032/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/c17568.png'],
            ['SCR - Soft Classic Rock', 'http://64.71.133.122:8000/', 'https://i46.servimg.com/u/f46/19/40/01/67/c17565.png'],
            ['Roots Legacy Radio', 'http://rootslegacy.fr:8080/stream/1/', 'https://i46.servimg.com/u/f46/19/40/01/67/c17566.png'],
            ['Puls Radio - Dance', 'http://icecast.pulsradio.com:80/pulsHD.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/pulsra10.jpg'],
            ['Puls Radio - Lounge', 'http://icecast.pulsradio.com/relaxHD.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/lounfe10.jpg'],
            ['Nostalgie Rock', 'http://cdn.nrjaudio.fm/adwz1/fr/30621/mp3_128.mp3?origine=radio.net', 'https://i46.servimg.com/u/f46/19/40/01/67/c17561.png']
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
            