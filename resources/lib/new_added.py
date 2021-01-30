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

        list = [        ['Rádio Play (CZ)', 'http://hydra.shoutca.st:8271/play', 'https://i46.servimg.com/u/f46/19/40/01/67/radiop12.jpg'],
         		['DAT Radio (CZ)', 'https://cast.beatzone.cz/radio/8110/radio.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/datrad10.jpg'],
         		['Atom FM (CZ)', 'http://212.84.160.187:4521/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/atomfm10.jpg'],
        		['Netro Life Radio (CZ)', 'https://icecast9.play.cz/netro-life-radio.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/netro-10.jpg'],  
                ['Comedy Club R@dio Diana (CZ)', 'https://westradio.cz/radio/8010/radio.mp3?1607941293', 'https://i46.servimg.com/u/f46/19/40/01/67/diana_10.jpg'],
                ['DNBTV.cz Rádio (CZ)', 'https://ice6.abradio.cz/dnbtv128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/dnbtv_10.jpg'],
                ['Radio Lovemusic (CZ)', 'http://solid55.streamupsolutions.com:32053/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/lm_rad10.jpg'],
                ['Rádio B (CZ)', 'https://n08.radiojar.com/9nayamd31tzuv?rj-ttl=5&rj-tok=AAABd1PLbWIACaXPhLOco5Al0w', 'https://i46.servimg.com/u/f46/19/40/01/67/becko10.jpg'],
                ['Bikers Radio Doupě (CZ)', 'http://icecast7.play.cz/bikersradiodoupe128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/bikers10.jpg'],
                ['tvojeRADIO.com Dance (SK)', 'https://radioserver.online:9816/dance.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiot13.jpg'],
			    ['tvojeRADIO.com Gold 80/90 (SK)', 'https://radioserver.online:9816/gold.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiot14.jpg'],
			    ['tvojeRADIO.com Hip-Hop (SK)', 'https://radioserver.online:9816/hiphop.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radioh10.jpg'],
			    ['tvojeRADIO.com Lovesongs (SK)', 'https://radioserver.online:9816/pohoda.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiot15.jpg'],
			    ['tvojeRADIO.com Pophits (SK)', 'https://radioserver.online:9816/pophits.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiot16.jpg'],
			    ['tvojeRADIO.com SK/CZ (SK)', 'https://radioserver.online:9816/skcz.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiot12.jpg'],
			    ['tvojeRADIO.com Repete (SK)', 'https://radioserver.online:9816/repete.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiot11.jpg'],
                ['FRESH rádio (SK)', 'https://freeuk23.listen2myradio.com/live.mp3?typeportmount=s2_9428_stream_641462344', 'https://i46.servimg.com/u/f46/19/40/01/67/fresh10.jpg']
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
