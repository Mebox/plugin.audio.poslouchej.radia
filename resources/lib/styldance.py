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
            ['Fresh Radio (SK)', 'http://164.68.122.137:8002/;stream/1', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_40.jpg'],
            ['Fun Rádio Dance (SK)', 'http://stream.funradio.sk:8000/dance128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiof23.jpg'],
            ['Rádio Kiks (SK)', 'http://ca6.rcast.net:4044/;stream/1', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_11.jpg'],
            ['Busradio (CZ)', 'http://mpc.mediacp.eu:8004/;type=mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/busrad10.jpg'],
            ['Club Rádio (CZ)', 'http://icecast2.play.cz:8000/Clubradio.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc18.jpg'],
            ['Clubbeat Rádio (CZ)', 'http://mp3stream4.abradio.cz/clubbeat128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc11.jpg'],
            ['DAB Plus Top 40 (CZ)', 'http://icecast6.play.cz/dabplus-top40.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiod12.jpg'],
            ['Dance Club Rádio (CZ)', 'http://mp3stream4.abradio.cz/dance128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/dancec11.jpg'],
            ['Dance Rádio (CZ)', 'http://ice.actve.net/dance-radio128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiod10.jpg'],
            ['Drumandbass Radio SHADOWBOX (CZ)', 'http://ice3.abradio.cz/shadowbox128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios10.jpg'],
            ['Freerave.cz - Tekno Radio (CZ)', 'http://164.68.122.137:8061/', 'https://i46.servimg.com/u/f46/19/40/01/67/freed10.jpg'],
            ['Radio23.cz - Techno (CZ)', 'http://r23.cz/tekno', 'https://i46.servimg.com/u/f46/19/40/01/67/radio210.jpg'],
            ['Radio23.cz - Breaks (CZ)', 'http://r23.cz/breaks', 'https://i46.servimg.com/u/f46/19/40/01/67/radio210.jpg'],
            ['Radio23.cz - Psytrance (CZ)', 'http://r23.cz/psy', 'https://i46.servimg.com/u/f46/19/40/01/67/radio210.jpg'],
            ['Radio23.cz - Dnb (CZ)', 'http://r23.cz/dnb', 'https://i46.servimg.com/u/f46/19/40/01/67/radio210.jpg'],
            ['Radio23.cz - Hardcore (CZ)', 'http://r23.cz/hc', 'https://i46.servimg.com/u/f46/19/40/01/67/radio210.jpg'],
            ['RadioCast (CZ)', 'https://mpc.mediacp.eu/stream/radiocast&error=ok', 'https://i46.servimg.com/u/f46/19/40/01/67/radioc10.jpg'],
            ['Rádio Chillout (CZ)', 'http://mp3stream4.abradio.cz/chillout128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc12.jpg'],
            ['Rádio Free 107 Fm (CZ)', 'http://icecast8.play.cz/freeradio128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiof23.jpg'],
            ['Fajn Radio Fresh (CZ)', 'http://ice.abradio.cz/fajnfresh128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiof12.jpg'],
            ['SeeJay Rádio (CZ)', 'http://mp3stream.abradio.cz:8000/seejay128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios11.jpg'],
            ['Rádio Spin 96,2 FM (CZ)', 'http://icecast4.play.cz/spin128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios14.jpg'],
            ['Radio Svit (CZ)', 'http://78.24.9.110:9490', 'https://i.servimg.com/u/f46/19/40/01/67/svit10.jpg'],
            ['This Is Radio (CZ)', 'http://ice3.abradio.cz/this_is_radio.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiot10.jpg'],
            ['Radio N-JOY (BG)', 'http://46.10.150.243/njoy.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radion12.jpg'],
            ['Dark Asylum Radio (GB)', 'http://91.121.165.137:8020/stream/1/', 'https://i46.servimg.com/u/f46/19/40/01/67/c175141.png'],
            ['KISS FM UK (GB)', 'http://icy-e-ba-01-gos.sharp-stream.com/kissnational.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175121.png'],
            ['NonStopPlay (GB)', 'http://stream.nonstopplay.co.uk/nsp-128k-mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175133.png'],
            ['NonStopPlay Pure Dance (GB)', 'http://stream.nonstopplay.co.uk/nsppd-128k-mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/nonsto10.jpg'],
            ['181.fm Party 181 (USA)', 'http://uplink.duplexfx.com:8036', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm POWER 181 (USA)', 'http://relay.181.fm:8128', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['Radio Danz (USA)', 'http://107.182.230.133/stream?icy=http', 'https://i62.servimg.com/u/f62/19/40/01/67/radio_13.png'],
            ['B4B Radio Club Dance (F)', 'https://radio10.pro-fhi.net/radio/9000/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/c17559.png'],
            ['Puls Radio Lounge (F)', 'http://icecast.pulsradio.com/relaxHD.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/lounfe10.jpg'],
            ['Mega Dance Radio (HU)', 'http://megadanceradio.hopto.org:8000/livemega.mp3?', 'https://i46.servimg.com/u/f46/19/40/01/67/mega_d10.jpg'],
            ['One Dance (I)', 'http://ice10.fluidstream.net/rn1_2.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175136.png'],
            ['Deep FM (NL)', 'http://stream.deep.radio/sd', 'https://i46.servimg.com/u/f46/19/40/01/67/c17579.png'],
            ['Antenne Bayern Fresh (D)', 'http://channels.webradio.antenne.de/fresh', 'https://i62.servimg.com/u/f62/19/40/01/67/antenn11.jpg'],
            ['M1.FM - Clubmix (D)', 'http://tuner.m1.fm/clubmix.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/clubmi10.jpg'],
            ['Kronehit Clubland xxl (A)', 'http://onair-ha1.krone.at/kronehit-clubland.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175132.png'],
            ['Kronehit Dance (A)', 'http://onair-ha1.krone.at/kronehit-dance.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175131.png'],
            ['16bit.FM - ProBeat (RU)', 'http://16bitfm.com:8000/main_mp3_192', 'https://i46.servimg.com/u/f46/19/40/01/67/c17538.png'],
            ['San FM - Trance Channel (RU)', 'http://sanfm.ru:8000/trance', 'https://i46.servimg.com/u/f46/19/40/01/67/c17539.png'],
            ['101.ru: Euro Hits (RU)', 'https://ic7.101.ru:8000/c16_13', 'https://static.radio.net/images/broadcasts/73/8a/7121/1/c300.png'],
            ['Energy Dance (CH)', 'http://energydance.ice.infomaniak.ch/energydance-high.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175134.png'],
            ['Rouge Dance (CH)', 'http://rouge-dance.ice.infomaniak.ch/rouge-dance-128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/rouge_10.jpg'],
            ['MyRadio Dance Club (UA)', 'http://music.myradio.com.ua:8000/dance128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c30010.png'],
            ['MyRadio Trance and Progressive (UA)', 'http://music.myradio.com.ua:8000/trance128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c30010.png']
            ]

        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?da_' + str(i), listitem=listItem, isFolder=True)
                i = i + 1
            xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
        else:
        
            Title = list[int(self.opt2)][0]
            Icon = list[int(self.opt2)][2]
            URL = list[int(self.opt2)][1]
        
            import radioPlayer as player
            player.Main().start(Title, Icon, URL)
            
