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
			['90 Hits Radio Manchester (CZ)', 'http://mpc.mediacp.eu:8012/;stream', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_37.jpg']
			['Busradio (CZ)', 'http://mpc.mediacp.eu:8004/;type=mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/busrad10.jpg'],
			['Calimeroclub Radio (CZ)', 'http://sc.ipip.cz:8052/', 'https://i46.servimg.com/u/f46/19/40/01/67/calime10.jpg'],
			['Fenix Radio Kanada (CZ)', 'https://maggie.torontocast.com:8006/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/fenix10.jpg'],
		        ['RadioCast (CZ)', 'http://mpc.mediacp.eu:8042/', 'https://i46.servimg.com/u/f46/19/40/01/67/radioc10.jpg'],
			['Rádio G6 (CZ)', 'https://mpc.mediacp.eu:2000/stream/RadioG6', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_36.jpg'],
        		['Rádio Ostravan (CZ)', 'http://icecast9.play.cz/radio-ostravan-256.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/ostrav10.jpg'],
        		['Rádio Stella (CZ)', 'https://ice3.abradio.cz/stella128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/rdio_s11.jpg'],
        		['Rádio Z (CZ)', 'https://ice.actve.net/fm-zet', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_38.jpg'],
         		['Svobodné Rádio (CZ)', 'http://svobodneradio.radioca.st:8859/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/svobod12.jpg']
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
