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
            ['Rádio Regina Západ (SK)', 'http://icecast.stv.livebox.sk/regina-ba_128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior10.jpg'],
            ['Rádio Regina Stred (SK)', 'http://icecast.stv.livebox.sk/regina-bb_128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior10.jpg'],
            ['Rádio Regina Východ (SK)', 'http://icecast.stv.livebox.sk/regina-ke_128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior10.jpg'],
            ['Slobodný vysielač (SK)', 'http://78.47.79.190:8004/;stream/1', 'https://i11.servimg.com/u/f11/19/40/01/67/radios18.jpg'],
            ['Rádio Slovakia International (SK)', 'http://icecast.stv.livebox.sk/rsi_128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radios15.jpg'],
            ['Rádio Slovensko (SK)', 'http://icecast.stv.livebox.sk/slovensko_128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radios12.jpg'],
            ['Rádio Šport (SK)', 'http://stream.radiosport.sk:8000/Sport192.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radios10.jpg'],
            ['Šport stream (SK)', 'http://play.sport-stream.sk:8000/sportstream128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios12.jpg'],
            ['Český rozhlas 1 - Rádiožurnál (CZ)', 'http://icecast8.play.cz/cro1-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior12.jpg'],
            ['Český rozhlas 2 - Praha (CZ)', 'http://icecast6.play.cz/cro2-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc22.jpg'],
            ['Český Rozhlas Brno (CZ)', 'http://icecast2.play.cz:8000/crobrno128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc28.jpg'],
            ['Český Rozhlas Hradec Králové (CZ)', 'http://icecast2.play.cz:8000/crohk128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc30.jpg'],
            ['Český Rozhlas Liberec (CZ)', 'http://icecast2.play.cz:8000/croliberec128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiol10.jpg'],
            ['Český Rozhlas Olomouc (CZ)', 'http://icecast2.play.cz:8000/crool128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc26.jpg'],
            ['Český Rozhlas Ostrava (CZ)', 'http://icecast2.play.cz:8000/croov128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc27.jpg'],
            ['Český Rozhlas Pardubice (CZ)', 'http://icecast2.play.cz:8000/cropardubice128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop19.jpg'],
            ['Český Rozhlas Plzeň studio Karlovy Vary (CZ)', 'http://icecast2.play.cz:8000/crokv128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/croplz13.png'],
            ['Český Rozhlas Plzeň (CZ)', 'http://icecast2.play.cz:8000/croplzen128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/croplz12.png'],
            ['Český Rozhlas Region - Vysočina (CZ)', 'http://icecast2.play.cz:8000/crovysocina128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/croreg10.png'],
            ['Český Rozhlas Sever (CZ)', 'http://icecast2.play.cz:8000/crosever128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios18.jpg'],
            ['Český Rozhlas České Budejovice (CZ)', 'http://icecast2.play.cz:8000/crocb128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc31.jpg'],
            ['Svobodný vysílač CS (CZ)', 'http://78.108.110.114:8000/live.opus', 'https://i46.servimg.com/u/f46/19/40/01/67/svobod11.jpg']
            ]

        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?zp_' + str(i), listitem=listItem, isFolder=True)
                i = i + 1
            xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
        else:
        
            Title = list[int(self.opt2)][0]
            Icon = list[int(self.opt2)][2]
            URL = list[int(self.opt2)][1]
        
            import radioPlayer as player
            player.Main().start(Title, Icon, URL)
            
