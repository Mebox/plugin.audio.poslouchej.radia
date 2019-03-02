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
            ['Rádio Devín (SK)', 'http://live.slovakradio.sk:8000/Devin_256.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiod11.jpg'],
            ['Rádio Janko Hraško (SK)', 'http://78.24.9.110:31088/;stream/1', 'https://i11.servimg.com/u/f11/19/40/01/67/radioj10.jpg'],
            ['Rádio Jemné Chillout (SK)', 'http://stream.radioservices.sk/chillout.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radioj12.jpg'],
            ['Rádio X - Chillout X (SK)', 'http://158.193.82.41:8000/chillout.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radioc10.jpg'],
            ['Classic Praha (CZ)', 'http://icecast8.play.cz/classic128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc34.jpg'],
            ['Český rozhlas 3 - Vltava (CZ)', 'http://icecast5.play.cz:8000/cro3-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc25.jpg'],
            ['Český Rozhlas D-dur (CZ)', 'http://icecast5.play.cz:8000/croddur-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiod18.jpg'],
            ['Koule.cz Filmové Melodie (CZ)', 'http://ice.actve.net/web-rb-melodie', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok14.jpg'],
            ['Proglas (CZ)', 'http://pool.cdn.lagardere.cz/web-pg-pohadky', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop17.jpg'],
            ['Rádio Chillout (CZ)', 'http://mp3stream4.abradio.cz/chillout128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc12.jpg'],
            ['Rádio Dechovka (CZ)', 'http://icecast5.play.cz:8000/dechovka128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiod13.jpg'],
            ['Rádio Jih - Cimbálka (CZ)', 'http://icecast6.play.cz/jihcimbalka128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioj13.jpg'],
            ['Relaxace - Jedoucí Vlak (CZ)', 'http://ice6.abradio.cz/relax-train128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior18.jpg'],
            ['Relaxace - Letná bouřka (CZ)', 'http://ice6.abradio.cz/relax-thunder-rain128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior20.jpg'],
            ['Relaxace - Oheň v krbu (CZ)', 'http://ice6.abradio.cz/relax-fire128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior21.jpg'],
            ['Relaxace - Relaxace - Moře (CZ)', 'http://ice6.abradio.cz/relax-sea128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior19.jpg'],
            ['Relaxace - Zpěv ptákú (CZ)', 'http://ice6.abradio.cz/relax-morning-birds128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior22.jpg'],
            ['BBC Radio 3 (GB)', 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio3_mf_q', 'https://i46.servimg.com/u/f46/19/40/01/67/c175145.png'],
            ['Chill (GB)', 'http://media-ice.musicradio.com/ChillMP3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175146.png'],
            ['Magic Chilled (GB)', 'https://stream-mz.planetradio.co.uk/magicchilled.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175139.png'],
            ['181.fm Classical Guitar (USA)', 'http://mp3uplink.duplexfx.com:8020', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['Antenne Bayern Chillout (D)', 'http://mp3channels.webradio.antenne.de/chillout', 'https://i62.servimg.com/u/f62/19/40/01/67/antena14.jpg'],
            ['Arabella Relax (A)', 'http://arabella.stream.kapper.net:8015/heroldrelax', 'https://i46.servimg.com/u/f46/19/40/01/67/c17521.png'],
            ['3 Music Harmony', 'http://misato.ru-hoster.com:8025/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/c17531.png'],
            ['Visual neoclassical Omdaru radio', 'http://s02.radio-tochka.com:5440/radio', 'https://i46.servimg.com/u/f46/19/40/01/67/c17542.png']
            ]

        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?re_' + str(i), listitem=listItem, isFolder=True)
                i = i + 1
            xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
        else:
        
            Title = list[int(self.opt2)][0]
            Icon = list[int(self.opt2)][2]
            URL = list[int(self.opt2)][1]
        
            import radioPlayer as player
            player.Main().start(Title, Icon, URL)
            
