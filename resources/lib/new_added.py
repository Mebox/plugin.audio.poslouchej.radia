  
﻿# -*- coding: utf-8 -*-

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
['FRESH rádio (SK)', 'https://freeuk23.listen2myradio.com/live.mp3?typeportmount=s2_9428_stream_641462344', 'https://i46.servimg.com/u/f46/19/40/01/67/fresh10.jpg],
['Comedy Club R@dio Diana (CZ)', 'https://westradio.cz/radio/8010/radio.mp3?1607941293', 'https://i46.servimg.com/u/f46/19/40/01/67/diana_10.jpg],
['DNBTV.cz Rádio (CZ)', 'https://ice6.abradio.cz/dnbtv128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/dnbtv_10.jpg'],
['Radio Lovemusic (CZ)', 'http://solid55.streamupsolutions.com:32053/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/lm_rad10.jpg'],
['Rádio B (CZ)', 'https://n08.radiojar.com/9nayamd31tzuv?rj-ttl=5&rj-tok=AAABd1PLbWIACaXPhLOco5Al0w', 'https://i46.servimg.com/u/f46/19/40/01/67/becko10.jpg'],
['Bikers Radio Doupě (CZ)', 'http://icecast7.play.cz/bikersradiodoupe128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/bikers10.jpg'],
['Rádio Cyp (CZ)', 'http://radio.radiocyp.cz:8000/;stream.nsv', 'https://i46.servimg.com/u/f46/19/40/01/67/radioc11.jpg'],
['Rádio Play (CZ)', 'http://hydra.shoutca.st:8271/play', 'https://i46.servimg.com/u/f46/19/40/01/67/radiop12.jpg'],
['DAT Radio (CZ)', 'https://cast.beatzone.cz/radio/8110/radio.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/datrad10.jpg'],
['Atom FM (CZ)', 'http://212.84.160.187:4521/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/atomfm10.jpg'],
['Netro Life Radio (CZ)', 'https://icecast9.play.cz/netro-life-radio.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/netro-10.jpg']
               ]

        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?new_' + str(i), listitem=listItem, isFolder=True)
                i = i + 1
            xbmcplugin.endOfDirectory(int(sys.argv[1]))

        else:

            Title = list[int(self.opt2)][0]
            Icon = list[int(self.opt2)][2]
            URL = list[int(self.opt2)][1]

            import radioPlayer as player
            player.Main().start(Title, Icon, URL)
