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
            ['101 Smooth Jazz Mellow Mix', 'https://edge3.peta.live365.net/b48071_128mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175149.png'],
            ['BBC Radio 1', 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_q', 'https://i46.servimg.com/u/f46/19/40/01/67/c175143.png'],
            ['BBC Radio 2', 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio2_mf_q', 'https://i46.servimg.com/u/f46/19/40/01/67/c175144.png'],
            ['BBC Radio 3', 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio3_mf_q', 'https://i46.servimg.com/u/f46/19/40/01/67/c175145.png'],
            ['Capital FM London', 'http://ice-sov.musicradio.com/CapitalMP3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175120.png'],
            ['Dark Asylum Radio', 'http://91.121.165.137:8020/stream/1/', 'https://i46.servimg.com/u/f46/19/40/01/67/c175141.png'],
            ['Diva Radio Disco', 'http://91.121.59.45:10114/live', 'https://i46.servimg.com/u/f46/19/40/01/67/divada10.jpg'],
            ['Gold', 'http://media-ice.musicradio.com/GoldMP3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175148.png'],
            ['Heart London', 'http://ice-sov.musicradio.com/HeartLondonMP3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175117.png'],
            ['Chill', 'http://media-ice.musicradio.com/ChillMP3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175146.png'],
            ['KISS FM UK', 'http://icy-e-ba-01-gos.sharp-stream.com/kissnational.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175121.png'],
            ['Magic Chilled', 'https://stream-mz.planetradio.co.uk/magicchilled.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175139.png'],
            ['Magic Soul', 'http://icy-e-bz-08-boh.sharp-stream.com/magicsoul.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175140.png'],
            ['NonStopPlay', 'http://stream.nonstopplay.co.uk/nsp-128k-mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175133.png'],
            ['NonStopPlay Pure Dance', 'http://stream.nonstopplay.co.uk/nsppd-128k-mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/nonsto10.jpg'],
            ['Radio City', 'http://icy-e-bl-09-boh.sharp-stream.com/city.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175151.png'],
            ['Radio City 2', 'https://stream-mz.planetradio.co.uk/magic1548.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175147.png'],
            ['Relaxing Jazz', 'http://stream-02-eu.relaxingjazz.com/stream/1/', 'https://i46.servimg.com/u/f46/19/40/01/67/c175150.png'],
            ['Virgin Radio UK', 'http://radio.virginradio.co.uk/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/c175122.png']
            ]

        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?uk_' + str(i), listitem=listItem, isFolder=True)
                i = i + 1
            xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
        else:
        
            Title = list[int(self.opt2)][0]
            Icon = list[int(self.opt2)][2]
            URL = list[int(self.opt2)][1]
        
            import radioPlayer as player
            player.Main().start(Title, Icon, URL)
    
