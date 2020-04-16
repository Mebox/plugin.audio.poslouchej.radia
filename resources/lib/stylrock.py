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
            ['Rádio Anténa Rock (SK)', 'http://stream.antenarock.sk/antena-hi.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior16.jpg'],
            ['Rádio Anténa Rock Hard (SK)', 'http://stream.radioservices.sk/hardrock.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior17.jpg'],
	    ['Rock Arena (SK)', 'http://icecast6.play.cz/rockarena.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/rockar10.png'],
	    ['Rádio X - Metal X (SK)', 'http://158.193.82.41:8000/metal.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiox11.jpg'],
            ['Hitrádio PopRock (CZ)', 'http://ice.abradio.cz/hitpoprock128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh11.jpg'],
            ['Metal Heart Rádio (CZ)', 'http://fr.radio-streamhosting.com:8000/metalheartradio128mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/metal_10.jpg'],
            ['Metalomanie (CZ)', 'http://ice.abradio.cz/metalomanie128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/metalm10.jpg'],
	    ['Rádio Beat (CZ)', 'http://icecast2.play.cz/radiobeat128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/beat10.png'],
            ['Rádio Best of Rock (CZ)', 'http://mp3stream4.abradio.cz/bestofrock128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiob10.jpg'],
            ['Rádio Čas Rock (CZ)', 'http://icecast7.play.cz:8000/casrock128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc23.jpg'],
            ['Rádio Oldies Rock (CZ)', 'http://mp3stream4.abradio.cz/oldiesrock128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior16.jpg'],
	    ['Rádio Orlicko 95,5 FM (CZ)', 'http://46.28.111.246/stream192.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/radioo10.jpg'],
	    ['Radio SoundWave (CZ)', 'http://81.91.84.138:8040', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_29.jpg'],
	    ['Radio Vambi (CZ)', 'https://node-15.zeno.fm/avzpd35rckeuv?rj-ttl=5&rj-tok=AAABcQzVTcMAWSQJ94pqkxNnqg', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_24.jpg'],
            ['Rebel Radio Brod (CZ)', 'http://212.96.160.160:7988/;stream.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/rebel_10.jpg'],
            ['Rock Rádio (CZ)', 'http://ice.abradio.cz:80/sumava128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior16.jpg'],
	    ['RockMax -Live (CZ)', 'http://212.111.2.151:8000/rockmax_128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior15.jpg'],
	    ['RockMax-Hard (CZ)', 'http://212.111.2.151:8000/rm_hard_256.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior15.jpg'],
	    ['RockMax-Oldies (CZ)', 'http://212.111.2.151:8000/rm_old_256.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior15.jpg'],
	    ['RockMax-Blue (CZ)', 'http://212.111.2.151:8000/rm_blue_128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior15.jpg'],
            ['RockZone 105,9 (CZ)', 'http://icecast2.play.cz/rockzone128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior22.jpg'],
            ['Rocková zábava (CZ)', 'http://ice.abradio.cz/rockzabava128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior10.jpg'],
	    ['West Radio (CZ)', 'https://node-16.zeno.fm/y6gyh7gg6heuv?rj-ttl=5&rj-tok=AAABcQ1G1YUAMgmz_r2kci4pLg', 'https://i46.servimg.com/u/f46/19/40/01/67/west-r10.jpg'],
            ['Známka Punku (CZ)', 'http://ice.abradio.cz/znamkapunku128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/znamen10.png'],
            ['181.fm 90s Alternative (USA)', 'http://uplink.duplexfx.com:8052', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm The Rock! (USA)', 'http://relay5.181.fm:8064', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['BeGoodRadio 80s Metal (USA)', 'http://75.126.5.154/5212_128', 'https://i11.servimg.com/u/f11/19/40/01/67/d4b66910.png'],
            ['BeGoodRadio 80s Punk Rock (USA)', 'http://75.126.5.154/5218_128', 'https://i11.servimg.com/u/f11/19/40/01/67/d4b66910.png'],
            ['BeGoodRadio 80s Rock Mix (USA)', 'http://75.126.5.154/5219_128', 'https://i11.servimg.com/u/f11/19/40/01/67/d4b66910.png'],
            ['Epic Rock Radio (USA)', 'http://listen.sonixfm.com:8734/stream', 'https://i11.servimg.com/u/f11/19/40/01/67/err-lo10.jpg'],
            ['RADIO TROP ROCK (USA)', 'http://usa14.fastcast4u.com:5224/stream/1/', 'https://i46.servimg.com/u/f46/19/40/01/67/c175129.png'],
            ['Third Rock Radio (USA)', 'http://rfcmedia2.streamguys1.com/thirdrock.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175126.png'],
            ['Underground fm (PL)', 'http://37.59.32.115:9100/stream#.mp3?ver=589796', 'https://i46.servimg.com/u/f46/19/40/01/67/underg11.png'],
            ['Underground fm - Metal Radio (PL)', 'http://37.59.32.115:9300/stream#.mp3?ver=650227', 'https://i46.servimg.com/u/f46/19/40/01/67/underg11.png'],
            ['Underground fm - Skinhead Radio (PL)', 'http://37.59.32.115:7769/stream#.mp3?ver=669520', 'https://i46.servimg.com/u/f46/19/40/01/67/underg11.png'],
            ['Underground fm - Polish Underground (PL)', 'http://37.59.32.115:9500/stream#.mp3?ver=167896', 'https://i46.servimg.com/u/f46/19/40/01/67/underg11.png'],
            ['M1.FM - Rock (D)', 'http://tuner.m1.fm/rock.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/rock-c10.jpg'],
            ['ANTENNE VORARLBERG Rock Radio (A)', 'http://webradio.antennevorarlberg.at/rock', 'https://i46.servimg.com/u/f46/19/40/01/67/c17527.png'],
            ['MAXXX Radio (RU)', 'http://46.105.180.202:8045/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/maxrad10.jpg'],
            ['Radio Caprice - AOR/Melodic Hard Rock (RU)', 'http://79.111.14.76:8000/aor', 'https://i46.servimg.com/u/f46/19/40/01/67/c17536.png'],
            ['Radio Caprice - Progressive Metal(RU)', 'http://79.120.77.11:8000/progmetal', 'https://i46.servimg.com/u/f46/19/40/01/67/c17535.png'],
            ['Rock FM - 80s (RU)', 'http://jfm1.hostingradio.ru:14536/rock80.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17590.png'],
            ['Rock FM - 90s (RU)', 'http://jfm1.hostingradio.ru:14536/rock90.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17590.png'],
            ['Rock FM - 00s (RU)', 'http://jfm1.hostingradio.ru:14536/rock00.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17590.png'],
            ['Rock FM - Heavy (RU)', 'http://jfm1.hostingradio.ru:14536/metal.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17590.png'],
            ['Radio Ultra 70.19 FM (RU)', 'http://nashe1.hostingradio.ru/ultra-128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17534.png']
	    ]

        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?ro_' + str(i), listitem=listItem, isFolder=True)
                i = i + 1
            xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
        else:
        
            Title = list[int(self.opt2)][0]
            Icon = list[int(self.opt2)][2]
            URL = list[int(self.opt2)][1]
        
            import radioPlayer as player
            player.Main().start(Title, Icon, URL)
            
