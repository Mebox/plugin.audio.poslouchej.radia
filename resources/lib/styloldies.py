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
            ['Rádio Beta - Hity 80s a 90s (SK)', 'http://109.71.67.102:8000/beta_80a90.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/beta8010.jpg'],
            ['Fun Rádio 80. - 90. roky (SK)', 'http://stream.funradio.sk:8000/80-90-128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiof21.jpg'],
            ['Rádio Goldies (SK)', 'http://icecast.radiosity.sk:8000/oldies.mp3', 'https://i.servimg.com/u/f46/19/40/01/67/goldie10.jpg'],
            ['Rádio Vlna Golden Hits (SK)', 'http://stream.radioservices.sk/goldenhits.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiov10.jpg'],
            ['Rádio X - Oldies X (SK)', 'http://158.193.82.41:8000/oldies.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiox10.jpg'],
	    ['90 Hits Radio Manchester (CZ)', 'http://mpc.mediacp.eu:8012/;stream', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_37.jpg'],
            ['Evropa 2 - Youradio Flashback (CZ)', 'http://ice.actve.net/web-e2-flashback', 'https://i46.servimg.com/u/f46/19/40/01/67/europa14.jpg'],
            ['Frekvence 1 - Youradio Legendy (CZ)', 'http://ice.actve.net/web-f1-legendy', 'https://i46.servimg.com/u/f46/19/40/01/67/f1_leg10.jpg'],
	    ['Frekvence 1 - Youradio 80s (CZ)', 'http://ice.actve.net/web-80', 'https://i62.servimg.com/u/f62/19/40/01/67/radiof21.jpg'],
            ['Impuls - Český Impuls (CZ)', 'http://icecast6.play.cz:8000/cesky-impuls.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioi13.jpg'],
            ['Hitrádio Osmdesátka (CZ)', 'http://ice.abradio.cz/hit80128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh11.jpg'],
            ['Hitrádio Devadesátka (CZ)', 'http://ice.abradio.cz/hit90128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh11.jpg'],
            ['Oldies rádio (CZ)', 'http://ice.abradio.cz/oldiesradio128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioo12.jpg'],
	    ['Radio Cesky Jukebox (CZ)', 'http://sc.ipip.cz:8046', 'https://i46.servimg.com/u/f46/19/40/01/67/radio-10.jpg'],
            ['Rádio MB (CZ)', 'http://icecast3.play.cz/radiomb.mp3', 'https://i.servimg.com/u/f46/19/40/01/67/radiom10.png'],
	    ['Rádio Nostalgie (CZ)', 'http://icecast3.play.cz/radio-nostalgie128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radion13.jpg'],
	    ['Radio O.K. (CZ)', 'https://node-10.zeno.fm/q7ura4u1akeuv?rj-ttl=5&rj-tok=AAABcQzZKFEAVyDUuNyclleYsg', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_25.jpg'],
            ['Signál Rádio (CZ)', 'http://icecast1.play.cz/signal128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios15.jpg'],
            ['Diva Radio Disco (GB)', 'http://91.121.59.45:10114/live', 'https://i46.servimg.com/u/f46/19/40/01/67/divada10.jpg'],
            ['Gold (GB)', 'http://media-ice.musicradio.com/GoldMP3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175148.png'],
            ['181.fm Lite 80s (USA)', 'http://relay.181.fm:8040?.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm 80s Hairband (USA)', 'http://mp3uplink.duplexfx.com:8014', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm 90s Alternative (USA)', 'http://uplink.duplexfx.com:8052', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm Star 90s (USA)', 'http://relay3.181.fm:8012', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['113 FM Awesome 80s (USA)', 'http://113fm-edge1.cdnstream.com/1762_128', 'https://i11.servimg.com/u/f11/19/40/01/67/113fm10.png'],
            ['Best Net Radio 70s and 80s (USA)', 'http://bigrradio.cdnstream1.com/5141_128', 'https://i46.servimg.com/u/f46/19/40/01/67/c175128.png'],
            ['Best Net Radio 80s and 90s Mix (USA)', 'http://bigrradio.cdnstream1.com/5143_128', 'https://i46.servimg.com/u/f46/19/40/01/67/c175128.png'],
            ['Hotmixradio 80 (F)', 'http://streaming.hotmixradio.fm/hotmixradio-80-128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17560.png'],
            ['E-Dance 90s (F)', 'http://94.23.221.158:9197/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/c17567.png'],
            ['Sky Radio 80s Hits (NL)', 'https://20133.live.streamtheworld.com/SRGSTR04.mp3?dist=radionet', 'https://i46.servimg.com/u/f46/19/40/01/67/c17592.png'],
            ['Sky Radio 90s Hits (NL)', 'https://playerservices.streamtheworld.com/api/livestream-redirect/SRGSTR05.mp3?dist=radionet', 'https://i46.servimg.com/u/f46/19/40/01/67/c17593.png'],
            ['Radio 10 Gold 60s 70s (NL) ', 'https://playerservices.streamtheworld.com/api/livestream-redirect/TLPSTR18.mp3?dist=radionet', 'https://i46.servimg.com/u/f46/19/40/01/67/c17577.png'],
            ['Radio Stad Den Haag 97.2 FM (NL)', 'http://94.228.133.3:80/;stream.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios19.jpg'],
            ['1 HITS 80s (D)', 'http://makri.cdnstream.com/1898_128', 'https://i46.servimg.com/u/f46/19/40/01/67/1_hits10.jpg'],
	    ['80s80s Italo Disco (D)', 'https://streams.80s80s.de/italohits/mp3-192/radiode/', 'https://i46.servimg.com/u/f46/19/40/01/67/c17585.png']
            ['Antenne Bayern 80er Kulthits (D)', 'http://mp3channels.webradio.antenne.de/80er-kulthits', 'https://i62.servimg.com/u/f62/19/40/01/67/antena16.jpg'],
            ['Antenne Bayern 90er Hits (D)', 'http://mp3channels.webradio.antenne.de/90er-hits', 'https://i62.servimg.com/u/f62/19/40/01/67/antena17.jpg'],
            ['Antenne Bayern Oldies but Goldies (D)', 'http://mp3channels.webradio.antenne.de/oldies-but-goldies', 'https://i62.servimg.com/u/f62/19/40/01/67/antena13.jpg'],
            ['Eurodance (D)', 'http://eurodance.stream.laut.fm/eurodance?ref=radiode&t302=2019-02-08_18-05-10&uuid=c432c351-3e28-4832-9332-38bb39e4b5e2', 'https://i46.servimg.com/u/f46/19/40/01/67/c175138.png'],
            ['Disco Party Radio (D)', 'http://stream.laut.fm/-z-i-s-c-o-party-70s-80s', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_33.jpg'],
            ['FFH Eurodance (D)', 'http://mp3.ffh.de/ffhchannels/hqeurodance.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/ffh_di11.jpg'],
            ['FFH - Die 80-er (D)', 'http://mp3.ffh.de/ffhchannels/hq80er.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/ffh_di10.jpg'],
            ['FFH - Just 90s (D)', 'http://mp3.ffh.de/ffhchannels/hq90er.aac', 'https://i11.servimg.com/u/f11/19/40/01/67/ffh_ju10.jpg'],
            ['M1.FM - Kuschelschlager (D)', 'http://tuner.m1.fm/kuschelschlager.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/m1fm1810.png'],
            ['M1.FM - Schlagerparty (D)', 'http://tuner.m1.fm/schlagerparty.mp3', 'https://i.servimg.com/u/f46/19/40/01/67/schlag10.jpg'],
            ['M1.FM - Oldies (D)', 'http://tuner.m1.fm/oldies.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/oldies10.jpg'],
            ['M1.FM - 80ER (D)', 'http://tuner.m1.fm/80er.mp3', 'https://i.servimg.com/u/f46/19/40/01/67/80er-c10.jpg'],
            ['M1.FM - 90ER (D)', 'http://tuner.m1.fm/90er.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/90er-c10.jpg'],
            ['Radio On Disco (D)', 'https://0n-disco.radionetz.de/0n-disco.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_32.jpg'],
	    ['OpenFM - 80s Hits (PL)', 'http://stream.polskastacja.pl/ps3_mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17532.png'],
            ['OpenFM - Italo Disco (PL)', 'https://stream.open.fm/27', 'https://i46.servimg.com/u/f46/19/40/01/67/c17580.png'],
            ['RMI - Italo Disco Greatest Hits (PL)', 'http://188.165.195.176:8046/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/c17528.png'],
            ['Kronehit 90’s Dance (A) ', 'http://onair-ha1.krone.at/kronehit-90sdance.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok16.jpg'],
            ['Life Radio 80er (A) ', 'https://stream.liferadio.at/80er/mp3-192/radioat', 'https://i46.servimg.com/u/f46/19/40/01/67/lifera11.jpg'],
            ['Life Radio 90er (A) ', 'https://stream.liferadio.at/90er/mp3-192/radioat', 'https://i46.servimg.com/u/f46/19/40/01/67/lifera12.jpg'],
	    ['101.ru: Radio 70s FM  (RU)', 'http://air2.radiorecord.ru:9002/1970_128', 'https://static.radio.net/images/broadcasts/73/8a/7121/1/c300.png'],
            ['101.ru: Radio 80s FM  (RU)', 'http://air2.radiorecord.ru:9002/1980_128', 'https://static.radio.net/images/broadcasts/73/8a/7121/1/c300.png'],
            ['Eurodisco Hit Radio (RU)', 'http://188.165.195.176:8034/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_30.jpg'],
	    ['Radio 70s FM (RU)', 'http://air2.radiorecord.ru:9002/1970_128', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_35.jpg'],
	    ['Radio 80s FM (RU)', 'http://air2.radiorecord.ru:9002/1980_128', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_34.jpg'],
	    ['Radio Obozrevatel Disco 80 (UA)', 'https://radio-stream-0.obozrevatel.com/Disco128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17584.png']
            ]

        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?ol_' + str(i), listitem=listItem, isFolder=True)
                i = i + 1
            xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
        else:
        
            Title = list[int(self.opt2)][0]
            Icon = list[int(self.opt2)][2]
            URL = list[int(self.opt2)][1]
        
            import radioPlayer as player
            player.Main().start(Title, Icon, URL)
            
