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
            ['KroneHit 105.8 FM', 'http://onair-ha1.krone.at/kronehit-hp.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok15.jpg'],
            ['Kronehit 90’s Dance', 'http://onair-ha1.krone.at/kronehit-90sdance.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok16.jpg'],
            ['Kronehit Beach Club', 'http://onair-ha1.krone.at/kronehit-event3.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok18.jpg'],
            ['Kronehit Black', 'http://onair-ha1.krone.at/kronehit-black.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok19.jpg'],
            ['Kronehit Charts', 'http://onair.krone.at/kronehit-charts.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok22.jpg'],
            ['Kronehit Love', 'http://onair-ha1.krone.at/kronehit-love.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/c17510.png'],
            ['KroneHit Best of 2017', 'http://onair.krone.at/kronehit-event3.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17510.png'],
            ['Life Radio Love', 'http://liferadio.stream.kapper.net:8003/lovelife', 'https://i46.servimg.com/u/f46/19/40/01/67/c17519.png'],
            ['VIENNA.AT - Lounge', 'http://webradio.vienna.at/vie-lounge', 'https://i46.servimg.com/u/f46/19/40/01/67/c17520.png'],
            ['Arabella Austropop', 'http://arabella.stream.kapper.net:8005/arabellaaustropop', 'https://i46.servimg.com/u/f46/19/40/01/67/c17526.png'],
            ['Arabella Ti Amo', 'http://arabella.stream.kapper.net:8007/arabellatiamo', 'https://i46.servimg.com/u/f46/19/40/01/67/c17525.png'],
            ['Arabella Relax', 'http://arabella.stream.kapper.net:8015/heroldrelax', 'https://i46.servimg.com/u/f46/19/40/01/67/c17521.png'],
            ['Arabella Lovesongs', 'http://arabella.stream.kapper.net:8009/arabellalove', 'https://i46.servimg.com/u/f46/19/40/01/67/c17523.png'],
            ['Arabella Oberösterreich', 'http://arabella.stream.kapper.net:8002/arabellaooe', 'https://i46.servimg.com/u/f46/19/40/01/67/c17524.png'],
            ['ANTENNE VORARLBERG', 'http://webradio.antennevorarlberg.at/live', 'https://i46.servimg.com/u/f46/19/40/01/67/c17518.png'],
            ['ANTENNE VORARLBERG Rock Radio', 'http://webradio.antennevorarlberg.at/rock', 'https://i46.servimg.com/u/f46/19/40/01/67/c17527.png'],
            ['ANTENNE VORARLBERG Partymix', 'http://webradio.antennevorarlberg.at/partymix', 'https://i46.servimg.com/u/f46/19/40/01/67/c17517.png'],
            ['ANTENNE VORARLBERG Love Songs', 'http://webradio.antennevorarlberg.at/lovesongs', 'https://i46.servimg.com/u/f46/19/40/01/67/c17516.png'],
            ['ANTENNE VORARLBERG Hits', 'http://webradio.antennevorarlberg.at/hits', 'https://i46.servimg.com/u/f46/19/40/01/67/c17515.png'],
            ['ANTENNE VORARLBERG 80er Hits', 'http://webradio.antennevorarlberg.at/80er', 'https://i46.servimg.com/u/f46/19/40/01/67/c17514.png'],
            ['Hitradio Ö3', 'https://oe3shoutcast.sf.apa.at/stream/1/', 'https://i46.servimg.com/u/f46/19/40/01/67/c17511.png']
            ]

        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?au_' + str(i), listitem=listItem, isFolder=True)
                i = i + 1
            xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
        else:
        
            Title = list[int(self.opt2)][0]
            Icon = list[int(self.opt2)][2]
            URL = list[int(self.opt2)][1]
        
            import radioPlayer as player
            player.Main().start(Title, Icon, URL)
            