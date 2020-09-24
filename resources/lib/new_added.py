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

        list = [        ['Fresh Radio (SK)', 'http://164.68.122.137:8002/;stream/1', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_40.jpg'],
         		['Rádio Dychovka (SK)', 'https://listen.radioking.com/radio/307817/stream/354746', 'https://i.servimg.com/u/f46/19/40/01/67/dychov10.jpg'],
        		['Rádio Mária Slovensko (SK)', 'https://dreamsiteradiocp5.com/proxy/radiomariaslovensko?mp=/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/maria10.jpg'],
			['90 Hits Radio Manchester (CZ)', 'http://mpc.mediacp.eu:8012/;stream', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_37.jpg'],
			['Busradio (CZ)', 'http://mpc.mediacp.eu:8004/;type=mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/busrad10.jpg'],
			['Calimeroclub Radio (CZ)', 'http://sc.ipip.cz:8052/', 'https://i46.servimg.com/u/f46/19/40/01/67/calime10.jpg'],
			['Fenix Radio Kanada (CZ)', 'https://maggie.torontocast.com:8006/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/fenix10.jpg'],
         		['Fred Film Radio (CZ)', 'http://stream.fred.fm:8026/stream/', 'https://i46.servimg.com/u/f46/19/40/01/67/fred10.jpg'],
		        ['Freerave.cz - Tekno Radio (CZ)', 'http://164.68.122.137:8061/', 'https://i46.servimg.com/u/f46/19/40/01/67/freed10.jpg'],
         		['Halloradio Hultschin (CZ)', 'http://live.halloradiohultschin.cz:8000/halloradio.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hallra10.jpg'],
		        ['RadioCast (CZ)', 'http://mpc.mediacp.eu:8042/', 'https://i46.servimg.com/u/f46/19/40/01/67/radioc10.jpg'],
			['Rádio G6 (CZ)', 'https://mpc.mediacp.eu:2000/stream/RadioG6', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_36.jpg'],
        		['Rádio Ostravan (CZ)', 'http://icecast9.play.cz/radio-ostravan-256.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/ostrav10.jpg'],
		        ['Radio R (CZ)', 'http://radior.video.muni.cz:8000/FSS_mp3-128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_39.jpg'],
        		['Radio Sailor (CZ)', 'https://node-26.zeno.fm/0wh8pvnyakeuv?rj-ttl=5&rj-tok=AAABdKyV0BgA4MI83O22J-L_Hg', 'https://i46.servimg.com/u/f46/19/40/01/67/rasdio10.jpg'],
        		['Rádio Z (CZ)', 'https://ice.actve.net/fm-zet', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_38.jpg'],
         		['Svobodné Rádio (CZ)', 'http://svobodneradio.radioca.st:8859/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/svobod12.jpg'],
		        ['True Life in God Radio Czech (CZ)', 'https://stream.galaxywebsolutions.com/proxy/tligradio_cs?mp=/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/tlig10.jpg'],
         		['OpenFM - Italo Disco (PL)', 'https://stream.open.fm/27', 'https://i46.servimg.com/u/f46/19/40/01/67/c17580.png'],
         		['Hit West 80s (F)', 'https://listen.shoutcast.com/HITWEST80.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17583.png'],
		        ['Radio Obozrevatel Disco 80 (UA)', 'https://radio-stream-0.obozrevatel.com/Disco128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17584.png'],
         		['80s80s Italo Disco (N)', 'https://streams.80s80s.de/italohits/mp3-192/radiode/', 'https://i46.servimg.com/u/f46/19/40/01/67/c17585.png']
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
