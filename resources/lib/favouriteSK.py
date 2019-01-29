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
            ['Rádio Expres', 'http://85.248.7.162:8000/96.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radioe15.jpg'],
			['Rádio Slovensko', 'http://icecast.stv.livebox.sk/slovensko_128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radios12.jpg'],
			['Fun Rádio', 'http://stream.funradio.sk:8000/fun128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiof20.jpg'],
			['Rádio Vlna', 'http://stream.radiovlna.sk/vlna-hi.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiov11.jpg'],
			['Europa 2', 'http://stream.radioservices.sk:50008/europa2.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radioe11.jpg'],
			['Rádio Regina Západ', 'http://icecast.stv.livebox.sk/regina-ba_128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior10.jpg'],
			['Rádio Jemné', 'http://stream.jemne.sk/jemne-hi.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radioj11.jpg'],
			['Rádio Anténa Rock', 'http://stream.antenarock.sk/antena-hi.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior16.jpg'],
			['Rádio_FM', 'http://icecast.stv.livebox.sk/fm_128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiof18.jpg'],
			['Rádio Lumen', 'http://audio.lumen.sk:8000/live128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiol10.jpg'],
            ]

        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?topSK_' + str(i), listitem=listItem, isFolder=True)
                i = i + 1
            xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
        else:
        
            Title = list[int(self.opt2)][0]
            Icon = list[int(self.opt2)][2]
            URL = list[int(self.opt2)][1]
        
            import radioPlayer as player
            player.Main().start(Title, Icon, URL)