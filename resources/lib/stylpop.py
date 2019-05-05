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
            ['Rádio Best FM (SK)', 'http://stream2.bestfm.sk:80/128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiob10.jpg'],
            ['Rádio Beta (SK)', 'http://109.71.67.102:8000/beta_live_high.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiob11.jpg'],
            ['Rádio Beta - České a Slovenské hity (SK)', 'http://109.71.67.102:8000/beta_cspop.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/betacz10.jpg'],
            ['Rádio Beta - Hráme Jubilantom (SK)', 'http://109.71.67.102:8000/beta_jubilanti.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/betaju10.jpg'],
            ['Radio Beta - Sladaky (SK)', 'http://109.71.67.102:8000/beta_sladaky.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/betasl10.jpg'],
            ['Rádio Blesk (SK)', 'http://stream.radioblesk.net:7777/;stream/1', 'https://i11.servimg.com/u/f11/19/40/01/67/radiob12.jpg'],
            ['Demomusic Rádio (SK)', 'http://server1.internetoveradio.sk:8977/;stream/1', 'https://i11.servimg.com/u/f11/19/40/01/67/radiod10.jpg'],
            ['Dobré Rádio (SK)', 'http://stream.dobreradio.sk:8813/dobreradio.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/dobrer10.jpg'],
            ['Europa2 SK (SK)', 'http://stream.radioservices.sk:50008/europa2.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radioe11.jpg'],
            ['Fun Rádio (SK)', 'http://stream.funradio.sk:8000/fun128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiof20.jpg'],
            ['Fun Rádio CZ-SK (SK)', 'http://stream.funradio.sk:8000/cs128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiof22.jpg'],
            ['Rádio Jemné (SK)', 'http://stream.jemne.sk/jemne-hi.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radioj11.jpg'],
            ['Rádio Jupiter (SK)', 'http://radio.treecom.net/jupiter_128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/radioj10.jpg'],
            ['Rádio Košice (SK)', 'http://194.145.206.131:8000/radiokosice-64.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiok12.jpg'],
            ['Rádio One (SK)', 'http://217.75.92.14:8000/nr160kb', 'https://i11.servimg.com/u/f11/19/40/01/67/radioo11.jpg'],
            ['Rádio Piešťany (SK)', 'http://live.radiopiestany.sk:8000/live.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiop12.jpg'],
            ['Rádio Plus (SK)', 'http://stream.sepia.sk:8000/plus128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiop10.jpg'],
            ['Rádio Rebeca (SK)', 'http://allnet.radionet.sk:8000/radiorebeca.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior14.jpg'],
            ['Rádio SiTy (SK)', 'http://icecast.radiosity.sk:8000/hq.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radios16.jpg'],
            ['SKY Rádio (SK)', 'http://stream.skyradio.sk:8000/sky128', 'https://i11.servimg.com/u/f11/19/40/01/67/radios17.jpg'],
            ['Trnavské rádio (SK)', 'http://stream.trnavskeradio.sk/trnavske', 'https://i62.servimg.com/u/f62/19/40/01/67/radiot12.jpg'],
            ['tvojeRADIO.com Lovesongs (SK)', 'http://server1.internetoveradio.sk:8816/pohoda.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiot15.jpg'],
            ['tvojeRADIO.com Pophits (SK)', 'http://server1.internetoveradio.sk:8816/pophits.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiot16.jpg'],
            ['tvojeRADIO.com SK/CZ (SK)', 'http://server1.internetoveradio.sk:8816/skcz.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiot12.jpg'],
            ['tvojeRADIO.com Repete (SK)', 'http://server1.internetoveradio.sk:8816/repete.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiot11.jpg'],
            ['Rádio Viva Metropol (SK)', 'http://stream.sepia.sk:8000/viva128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiov12.jpg'],
            ['Rádio Valec (SK)', 'http://radiovalec.out.airtime.pro:8000/radiovalec_a', 'https://i46.servimg.com/u/f46/19/40/01/67/radiov10.jpg'],
            ['Rádio Vlna (SK)', 'http://stream.radiovlna.sk/vlna-hi.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiov11.jpg'],
            ['Rádio WOW (SK)', 'http://stream.radiowow.sk:8200/', 'https://i11.servimg.com/u/f11/19/40/01/67/radiow10.jpg'],
            ['Rádio Yes (SK)', 'http://80.242.44.249:8000/;stream/1', 'https://i11.servimg.com/u/f11/19/40/01/67/radioy12.jpg'],
            ['Záhorácke Rádio (SK)', 'http://live.zahorackeradio.sk:8000/zr128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radioz10.jpg'],
            ['COOP TIP Rádio (CZ)', 'http://ice4.abradio.cz/coop128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc16.jpg'],
            ['Coop TUTY Rádio (CZ)', 'http://ice4.abradio.cz/cooptuty128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/tuty10.png'],
            ['Evropa 2 (CZ)', 'http://icecast3.play.cz/evropa2-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioe11.jpg'],
            ['Evropa 2 - Youradio HOT (CZ)', 'http://ice.actve.net/web-e2-hot', 'https://i46.servimg.com/u/f46/19/40/01/67/europa11.jpg'],
            ['Evropa 2 - Youradio Top 40 (CZ)', 'http://ice.actve.net/web-e2-top40', 'https://i46.servimg.com/u/f46/19/40/01/67/europa12.jpg'],
            ['Evropa 2 - Youradio Československé hity (CZ)', 'http://ice.actve.net/web-e2-csweb', 'https://i46.servimg.com/u/f46/19/40/01/67/europa10.jpg'],
            ['Fajn Radio (CZ)', 'http://ice.abradio.cz/fajn128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiof13.jpg'],
            ['Frekvence 1 (CZ)', 'http://icecast4.play.cz/frekvence1-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiof16.jpg'],
            ['Helax 93,7 (CZ)', 'http://ice.abradio.cz:8000/helax128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh10.jpg'],
            ['Hitrádio FM Plus (CZ)', 'http://ice.abradio.cz/fmplus128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitrad14.jpg'],
            ['Hitrádio FM (CZ)', 'http://ice.abradio.cz/hitradiofm128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitrad15.jpg'],
            ['Hitrádio Faktor (CZ)', 'http://ice.abradio.cz/faktor128a.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitrad13.jpg'],
            ['Hitrádio Magic (CZ)', 'http://ice.abradio.cz/magic128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitrad12.jpg'],
            ['Hitrádio City (CZ)', 'http://ice.abradio.cz/citybrno128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitcit10.jpg'],
            ['Hitrádio City Zóna lásky (CZ)', 'http://ice.abradio.cz/cityzl128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh18.jpg'],
            ['Hitrádio PopRock (CZ)', 'http://ice.abradio.cz/hitpoprock128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh11.jpg'],
            ['Radio City milenium (CZ)', 'http://ice.abradio.cz/citymi128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh17.jpg'],
	    ['Hitrádio Černá Hora (CZ)', 'http://ice.abradio.cz/cernahora128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitrad16.jpg'],
	    ['Hitrádio Orion (CZ)', 'http://ice.abradio.cz/orion128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitcit12.jpg'],
	    ['Hitrádio Vysočina (CZ)', 'http://ice5.abradio.cz/hitvysocina128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitcit13.jpg'],
	    ['Hitrádio Dragon (CZ)', 'http://ice.abradio.cz/dragon128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitcit11.jpg'],
	    ['Impuls Rádio (CZ)', 'http://icecast5.play.cz/impuls128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioi12.jpg'],
            ['Impuls - Český Impuls (CZ)', 'http://icecast6.play.cz:8000/cesky-impuls.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioi13.jpg'],
            ['Rádio Benešov City (CZ)', 'http://ice6.abradio.cz/benesov128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/beneso10.png'],
	    ['Rádio Blaník (CZ)', 'http://ice.abradio.cz/blanikfm128.mp3?i=86.22812972256186', 'https://i62.servimg.com/u/f62/19/40/01/67/radiob12.jpg'],
            ['Radio Blanik Cz (CZ)', 'http://ice.abradio.cz/blanikcz128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiob12.jpg'],
            ['Rádio Bonton (CZ)', 'http://icecast3.play.cz/bonton-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiob13.jpg'],
	    ['Rádio Contact Liberec (CZ)', 'http://icecast8.play.cz/contact128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc21.jpg'], 
	    ['Rádio Čas (Brno) (CZ)', 'http://icecast7.play.cz:8000/casbrno128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc24.jpg'],
            ['Rádio Čas (Ostrava) (CZ)', 'http://icecast7.play.cz:8000/casradio128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc24.jpg'],
	    ['Rádio Expert (CZ)', 'http://mp3stream3.abradio.cz/expert-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioe10.jpg'],
	    ['Rádio Golf (CZ)', 'http://ice4.abradio.cz/golf128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiog11.jpg'],
	    ['Rádio Haná (CZ)', 'http://icecast8.play.cz/hana160.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh19.jpg'],
	    ['Rádio JIH (CZ)', 'http://icecast6.play.cz/jih128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioj11.jpg'],
	    ['Rádio Kiss (CZ)', 'http://icecast4.play.cz:8000/kiss128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok13.jpg'],
	    ['Rádio Krokodýl (CZ)', 'http://icecast4.play.cz/krokodyl128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok11.jpg'],
	    ['Rádio Kroměříž (CZ)', 'http://icecast6.play.cz/radio-kromeriz128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok12.jpg'],
	    ['Rádio Merkur (CZ)', 'http://ice4.abradio.cz/merkur-casino128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiom12.jpg'],
	    ['Rádio Petrov (CZ)', 'http://icecast6.play.cz:8000/petrov128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop14.jpg'],
	    ['Rádio Radnice (CZ)', 'http://ice3.abradio.cz/radnice128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior11.jpg'],
	    ['Rádio Rubi (CZ)', 'http://icecast8.play.cz/radiorubi128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior21.jpg'],
	    ['Rádio Zlín (CZ)', 'http://212.111.2.151:8000/radiozlin_256.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioz11.jpg'],
	    ['Signál Rádio (CZ)', 'http://icecast1.play.cz/signal128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios15.jpg'],
	    ['Signál Rádio Brno (CZ)', 'http://icecast3.play.cz/signal-brno192.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios15.jpg'],
	    ['BBC Radio 2 (GB)', 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio2_mf_q', 'https://i46.servimg.com/u/f46/19/40/01/67/c175144.png'],
	    ['Capital FM London (GB)', 'http://ice-sov.musicradio.com/CapitalMP3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175120.png'],
	    ['Radio City (GB)', 'http://icy-e-bl-09-boh.sharp-stream.com/city.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175151.png'],
	    ['Radio City 2 (GB)', 'https://stream-mz.planetradio.co.uk/magic1548.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175147.png'],
	    ['Best Net Radio Love Channel (USA)', 'http://bigrradio.cdnstream1.com/5161_128', 'https://i46.servimg.com/u/f46/19/40/01/67/c175128.png'],
	    ['Powerhitz (USA)', 'http://powerhitz.powerhitz.com:2228?.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop15.jpg'],
	    ['Powerhitz - The Hitlist (USA)', 'http://jbmedia-edge1.cdnstream.com/hitlist?cb=718368.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop15.jpg'],
	    ['Hotmixradio HITS (F)', 'http://streaming.hotmixradio.fm/hotmixradio-hits-128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17572.png'],
            ['Hotmixradio 2000 (F)', 'http://streaming.hotmixradio.fm/hotmixradio-2k-128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17573.png'],
	    ['RTL2 (F)', 'http://streaming.radio.rtl2.fr/rtl2-1-48-192', 'https://i46.servimg.com/u/f46/19/40/01/67/c17569.png'],
	    ['Sky Radio 101 FM (NL)', 'https://playerservices.streamtheworld.com/api/livestream-redirect/SKYRADIO.mp3?dist=radionet', 'https://i46.servimg.com/u/f46/19/40/01/67/c17575.png'],
	    ['Sky Radio Hits (NL)', 'https://playerservices.streamtheworld.com/api/livestream-redirect/SRGSTR01.mp3?dist=radionet', 'https://i46.servimg.com/u/f46/19/40/01/67/c17595.png'],
            ['Sky Radio 10s Hits (NL)', 'https://playerservices.streamtheworld.com/api/livestream-redirect/SRGSTR19.mp3?dist=radionet', 'https://i46.servimg.com/u/f46/19/40/01/67/c17575.png'],
            ['Sky Radio Summerhits (NL)', 'https://playerservices.streamtheworld.com/api/livestream-redirect/SRGSTR02.mp3?dist=radionet', 'https://i46.servimg.com/u/f46/19/40/01/67/c17575.png'],
	    ['Antenne Bayern (D)', 'http://mp3channels.webradio.antenne.de/antenne', 'https://i62.servimg.com/u/f62/19/40/01/67/antena10.jpg'],
	    ['Antenne Bayern Top 40 (D)', 'http://mp3channels.webradio.antenne.de/top-40', 'https://i62.servimg.com/u/f62/19/40/01/67/antena12.jpg'],
	    ['Antenne Bayern Lovesongs (D)', 'http://mp3channels.webradio.antenne.de/lovesongs', 'https://i62.servimg.com/u/f62/19/40/01/67/f3c7d910.jpg'],
	    ['FFH Digital (D)', 'http://mp3.ffh.de/radioffh/hqlivestream.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/ffh_di10.jpg'],
	    ['FFH Top 40 (D)', 'http://mp3.ffh.de/ffhchannels/hqtop40.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/ffh_di12.jpg'],
            ['ANTENNE VORARLBERG (A)', 'http://webradio.antennevorarlberg.at/live', 'https://i46.servimg.com/u/f46/19/40/01/67/c17518.png'],
            ['ANTENNE VORARLBERG Love Songs (A)', 'http://webradio.antennevorarlberg.at/lovesongs', 'https://i46.servimg.com/u/f46/19/40/01/67/c17516.png'],
            ['ANTENNE VORARLBERG Hits (A)', 'http://webradio.antennevorarlberg.at/hits', 'https://i46.servimg.com/u/f46/19/40/01/67/c17515.png'],
	    ['Arabella Austropop (A)', 'http://arabella.stream.kapper.net:8005/arabellaaustropop', 'https://i46.servimg.com/u/f46/19/40/01/67/c17526.png'],
            ['Arabella Lovesongs (A)', 'http://arabella.stream.kapper.net:8009/arabellalove', 'https://i46.servimg.com/u/f46/19/40/01/67/c17523.png'],
            ['Arabella Oberösterreich (A)', 'http://arabella.stream.kapper.net:8002/arabellaooe', 'https://i46.servimg.com/u/f46/19/40/01/67/c17524.png'],
            ['KroneHit 105.8 FM (A)', 'http://onair-ha1.krone.at/kronehit-hp.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok15.jpg'],
	    ['Kronehit Love (A)', 'http://onair-ha1.krone.at/kronehit-love.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/c17510.png'],
            ['KroneHit Best of 2017 (A)', 'http://onair.krone.at/kronehit-event3.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17510.png'],
	    ['Hitradio Ö3 (A)', 'https://oe3shoutcast.sf.apa.at/stream/1/', 'https://i46.servimg.com/u/f46/19/40/01/67/c17511.png'],
            ['Life Radio (A)', 'http://liferadio.stream.kapper.net:8000/liferadio', 'https://i46.servimg.com/u/f46/19/40/01/67/lifera10.jpg'],
            ['Life Radio Love (A)', 'http://liferadio.stream.kapper.net:8007/livesongs', 'https://i46.servimg.com/u/f46/19/40/01/67/c17519.png'],
	    ['AvtoRadio (RU)', 'http://ic7.101.ru:8000/v3_1', 'https://i46.servimg.com/u/f46/19/40/01/67/c17529.png'],
            ['Best FM Moscow (RU)', 'http://nashe1.hostingradio.ru/best-128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17530.png'],
            ['Europa Plus ru (RU)', 'http://ep256.hostingradio.ru:8052/europaplus256.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17533.png'],
            ['NRJ 104.2 FM Moscow (RU)', 'http://ic7.101.ru:8000/v1_1', 'https://i46.servimg.com/u/f46/19/40/01/67/c17537.png'],
	    ['IP music (CH)', 'http://live9.avf.ch:8000/ipmusicaacplus128', 'https://i62.servimg.com/u/f62/19/40/01/67/radioi11.jpg']
            ]

        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?po_' + str(i), listitem=listItem, isFolder=True)
                i = i + 1
            xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
        else:
        
            Title = list[int(self.opt2)][0]
            Icon = list[int(self.opt2)][2]
            URL = list[int(self.opt2)][1]
        
            import radioPlayer as player
            player.Main().start(Title, Icon, URL)
            
