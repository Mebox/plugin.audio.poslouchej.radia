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
<<<<<<< Updated upstream
    
        list = [
            ['90 Hits Radio Manchester', 'http://mpc.mediacp.eu:8012/;stream', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_37.jpg'],
		        ['Alternative Times Radio', 'http://ice3.abradio.cz/alternative128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioa10.jpg'],
         		['Atom FM', 'http://212.84.160.187:4521/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/atomfm10.jpg'],
		        ['Bikers Radio Doupě', 'http://icecast7.play.cz/bikersradiodoupe128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/bikers10.jpg'],
		        ['Blues Sky', 'https://node-05.zeno.fm/0hx4b9zscseuv?rj-ttl=5&rj-tok=AAABcQzR__wA_g1Ji3kf17PHog', 'https://i46.servimg.com/u/f46/19/40/01/67/blues_10.jpg'],
		        ['Busradio', 'http://mpc.mediacp.eu:8004/;type=mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/busrad10.jpg'],
			['Classic Praha', 'http://icecast8.play.cz/classic128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc34.jpg'],
		        ['Calimeroclub Radio', 'http://sc.ipip.cz:8052/', 'https://i46.servimg.com/u/f46/19/40/01/67/calime10.jpg'],
			['Club Rádio', 'http://icecast2.play.cz:8000/Clubradio.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc18.jpg'],
			['COLOR Music Radio', 'http://icecast6.play.cz/color192.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc19.jpg'],
			['Country Rádio', 'http://icecast4.play.cz/country128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc33.jpg'],
                        ['COOP TIP Rádio', 'http://ice4.abradio.cz/coop128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc16.jpg'],
                        ['Coop TUTY Rádio', 'http://ice4.abradio.cz/cooptuty128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/tuty10.png'],
                        ['Český rozhlas 1 - Rádiožurnál', 'http://icecast8.play.cz/cro1-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior12.jpg'],
			['Český rozhlas 2 - Praha', 'http://icecast6.play.cz/cro2-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc22.jpg'],
			['Český rozhlas 3 - Vltava', 'http://icecast5.play.cz:8000/cro3-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc25.jpg'],
			['Český Rozhlas Brno', 'http://icecast2.play.cz:8000/crobrno128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc28.jpg'],
			['Český Rozhlas Regina DAB Praha', 'http://icecast2.play.cz:8000/croregina128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc32.jpg'],
			['Český Rozhlas D-dur', 'http://icecast5.play.cz:8000/croddur-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiod18.jpg'],
			['Český Rozhlas Hradec Králové', 'http://icecast2.play.cz:8000/crohk128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc30.jpg'],
			['Český Rozhlas Jazz', 'http://icecast2.play.cz:8000/crojazz128aac', 'https://i62.servimg.com/u/f62/19/40/01/67/radioj14.jpg'],
			['Český Rozhlas Liberec', 'http://icecast2.play.cz:8000/croliberec128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiol10.jpg'],
			['Český Rozhlas Olomouc', 'http://icecast2.play.cz:8000/crool128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc26.jpg'],
			['Český Rozhlas Ostrava', 'http://icecast2.play.cz:8000/croov128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc27.jpg'],
			['Český Rozhlas Pardubice', 'http://icecast2.play.cz:8000/cropardubice128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop19.jpg'],
			['Český Rozhlas Plus', 'http://icecast1.play.cz/croplus128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop18.jpg'],
			['Český Rozhlas Plzeň studio Karlovy Vary', 'http://icecast2.play.cz:8000/crokv128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/croplz13.png'],
			['Český Rozhlas Plzeň', 'http://icecast2.play.cz:8000/croplzen128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/croplz12.png'],
			['Český Rozhlas Regina DAB Praha', 'http://icecast2.play.cz:8000/croregina128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc32.jpg'],
			['Český Rozhlas Region - Vysočina', 'http://icecast2.play.cz:8000/crovysocina128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/croreg10.png'],
			['Český Rozhlas Region Stredočeský kraj', 'http://icecast2.play.cz:8000/croregion128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiov12.jpg'],
			['Český Rozhlas Sever', 'http://icecast2.play.cz:8000/crosever128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios18.jpg'],
			['Český Rozhlas Wave', 'http://icecast5.play.cz:8000/crowave-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiow10.jpg'],
			['Český Rozhlas České Budejovice', 'http://icecast2.play.cz:8000/crocb128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc31.jpg'],
                        ['Český Rozhlas Rádio Junior Písničky', 'http://icecast7.play.cz/crojuniormini128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc29.jpg'],
                        ['Český Rozhlas Rádio Junior', 'http://icecast5.play.cz:8000/crojuniormaxi128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioj15.jpg'],
                        ['Český Rozhlas Rádio Retro', 'http://ice3.abradio.cz/croretro128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior13.jpg'],
         		['Comedy Club R@dio Diana', 'https://westradio.cz/radio/8010/radio.mp3?1607941293', 'https://i46.servimg.com/u/f46/19/40/01/67/diana_10.jpg'],
                        ['DAB Plus Top 40', 'http://icecast6.play.cz/dabplus-top40.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiod12.jpg'],
                        ['Dance Club Rádio', 'http://mp3stream4.abradio.cz/dance128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/dancec11.jpg'],
			['Dance Rádio', 'http://ice.actve.net/dance-radio128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiod10.jpg'],
         		['DAT Radio', 'https://cast.beatzone.cz/radio/8110/radio.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/datrad10.jpg'],
         		['DNBTV.cz Rádio', 'https://ice6.abradio.cz/dnbtv128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/dnbtv_10.jpg'],
			['Drumandbass Radio SHADOWBOX', 'http://ice3.abradio.cz/shadowbox128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios10.jpg'],
			['E-Radio JAZZINEC', 'http://ice3.abradio.cz/jazzinec128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioj10.jpg'],
			['Evropa 2', 'http://ice.actve.net/fm-evropa2-128', 'https://i62.servimg.com/u/f62/19/40/01/67/radioe11.jpg'],
                        ['Evropa 2 - Youradio HOT', 'http://ice.actve.net/web-e2-hot', 'https://i46.servimg.com/u/f46/19/40/01/67/europa11.jpg'],
                        ['Evropa 2 - Youradio Top 40', 'http://ice.actve.net/web-e2-top40', 'https://i46.servimg.com/u/f46/19/40/01/67/europa12.jpg'],
                        ['Evropa 2 - Youradio Movin', 'http://ice.actve.net/web-e2-movin', 'https://i46.servimg.com/u/f46/19/40/01/67/europa13.jpg'],
                        ['Evropa 2 - Youradio Československé hity', 'http://ice.actve.net/web-e2-csweb', 'https://i46.servimg.com/u/f46/19/40/01/67/europa10.jpg'],
                        ['Evropa 2 - Youradio Flashback', 'http://ice.actve.net/web-e2-flashback', 'https://i46.servimg.com/u/f46/19/40/01/67/europa14.jpg'],
			['Expres FM', 'http://icecast8.play.cz/expres128mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/expres10.png'],
                        ['Fajn Radio', 'http://ice.abradio.cz/fajn128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiof13.jpg'],
                        ['Fajn Radio Fresh', 'http://ice.abradio.cz/fajnfresh128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiof12.jpg'],
		        ['Fenix Radio Kanada', 'https://maggie.torontocast.com:8006/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/fenix10.jpg'],
			['Frekvence 1', 'http://ice.actve.net/fm-frekvence1-128', 'https://i62.servimg.com/u/f62/19/40/01/67/radiof16.jpg'],
			['Frekvence 1 - Youradio Legendy', 'http://ice.actve.net/web-f1-legendy', 'https://i46.servimg.com/u/f46/19/40/01/67/f1_leg10.jpg'],
			['Frekvence 1 - Youradio 80s', 'http://ice.actve.net/web-80', 'https://i62.servimg.com/u/f62/19/40/01/67/radiof21.jpg'],
         		['Fred Film Radio', 'http://stream.fred.fm:8026/stream/', 'https://i46.servimg.com/u/f46/19/40/01/67/fred10.jpg'],
		        ['Freerave.cz - Tekno Radio', 'http://164.68.122.137:8061/', 'https://i46.servimg.com/u/f46/19/40/01/67/freed10.jpg'],
		        ['Funkstar Radio', 'https://funkstar.radioca.st/stream?ver=153586', 'https://i46.servimg.com/u/f46/19/40/01/67/funkst10.jpg'],
         		['Halloradio Hultschin', 'http://live.halloradiohultschin.cz:8000/halloradio.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hallra10.jpg'],
			['HEY Radio', 'http://icecast3.play.cz/hey-radio128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh20.jpg'],
			['Helax 93,7', 'http://ice.abradio.cz:8000/helax128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh10.jpg'],
			['HipHopVibes Rádio', 'http://mp3stream4.abradio.cz/hiphopvibes128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh14.jpg'],
			['Hitrádio FM Plus', 'http://ice.abradio.cz/fmplus128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitrad14.jpg'],
			['Hitrádio FM', 'http://ice.abradio.cz/hitradiofm128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitrad15.jpg'],
			['Hitrádio Faktor', 'https://playerservices.streamtheworld.com/api/livestream-redirect/HITRADIO_FAKTOR_128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitrad13.jpg'],
			['Hitrádio Magic', 'http://ice.abradio.cz/magic128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitrad12.jpg'],
                        ['Hitrádio City (Brno)', 'http://ice.abradio.cz/citybrno128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitcit10.jpg'],
			['Hitrádio City (Praha)', 'http://ice.abradio.cz:8000/cityfm128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitcit10.jpg'],			
			['Hitrádio City Zóna lásky', 'http://ice.abradio.cz/cityzl128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh18.jpg'],
			['Hitrádio PopRock', 'http://ice.abradio.cz/hitpoprock128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh11.jpg'],
			['Hitrádio Osmdesátka', 'http://ice.abradio.cz/hit80128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh11.jpg'],
			['Hitrádio Devadesátka', 'http://ice.abradio.cz/hit90128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh11.jpg'],
                        ['Radio City milenium', 'http://ice.abradio.cz/citymi128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh17.jpg'],
			['Hitrádio Černá Hora', 'https://20423.live.streamtheworld.com/HITRADIO_CERNAHORA_128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitrad16.jpg'],
			['Hitrádio Orion', 'http://ice.abradio.cz/orion128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitcit12.jpg'],
			['Hitrádio Vysočina', 'http://ice5.abradio.cz/hitvysocina128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitcit13.jpg'],
			['Hitrádio Dragon', 'http://ice.abradio.cz/dragon128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitcit11.jpg'],
			['Impuls Rádio', 'http://icecast5.play.cz/impuls128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioi12.jpg'],
                        ['Impuls - Český Impuls', 'http://icecast6.play.cz:8000/cesky-impuls.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioi13.jpg'],
			['Koule.cz Filmové Melodie', 'http://ice.actve.net/web-rb-melodie', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok14.jpg'],
		        ['Metal Heart Rádio', 'http://fr.radio-streamhosting.com:8000/metalheartradio128mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/metal_10.jpg'],
			['Metalomanie', 'http://ice.abradio.cz/metalomanie128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/metalm10.jpg'],
         		['Netro Life Radio', 'https://icecast9.play.cz/netro-life-radio.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/netro-10.jpg'],
			['Oldies rádio', 'http://ice.abradio.cz/oldiesradio128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioo12.jpg'],
			['Pigy.cz - Disko Trysko', 'http://ice.actve.net/web-pg-disko', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop10.jpg'],
			['Pigy.cz - Písničky z Pohádek', 'http://ice.actve.net/web-pg-pisnicky', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop10.jpg'],
			['Pigy.cz - Pohádky', 'http://ice.actve.net/web-pg-pohadky', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop10.jpg'],
			['Proglas', 'http://icecast2.play.cz/proglas128', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop17.jpg'],
		        ['Radio23.cz - Techno', 'http://r23.cz/tekno', 'https://i46.servimg.com/u/f46/19/40/01/67/radio210.jpg'],
                        ['Radio23.cz - Breaks', 'http://r23.cz/breaks', 'https://i46.servimg.com/u/f46/19/40/01/67/radio210.jpg'],
                        ['Radio23.cz - Psytrance', 'http://r23.cz/psy', 'https://i46.servimg.com/u/f46/19/40/01/67/radio210.jpg'],
                        ['Radio23.cz - Dnb', 'http://r23.cz/dnb', 'https://i46.servimg.com/u/f46/19/40/01/67/radio210.jpg'],
                        ['Radio23.cz - Hardcore', 'http://r23.cz/hc', 'https://i46.servimg.com/u/f46/19/40/01/67/radio210.jpg'],
		        ['RadioCast', 'https://mpc.mediacp.eu/stream/radiocast&error=ok', 'https://i46.servimg.com/u/f46/19/40/01/67/radioc10.jpg'],
		        ['Radio Cesky Jukebox', 'http://sc.ipip.cz:8046', 'https://i46.servimg.com/u/f46/19/40/01/67/radio-10.jpg'],
         		['Rádio B (CZ)', 'https://n08.radiojar.com/9nayamd31tzuv?rj-ttl=5&rj-tok=AAABd1PLbWIACaXPhLOco5Al0w', 'https://i46.servimg.com/u/f46/19/40/01/67/becko10.jpg'],
			['Rádio Benešov City', 'http://ice6.abradio.cz/benesov128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/beneso10.png'],
			['Rádio Best of Rock', 'http://mp3stream4.abradio.cz/bestofrock128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiob10.jpg'],
			['Rádio Beat', 'http://icecast2.play.cz/radiobeat128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/beat10.png'],
			['Rádio Best of Rock', 'http://mp3stream4.abradio.cz/bestofrock128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiob10.jpg'],
			['Rádio Blaník', 'http://ice.abradio.cz/blanikfm128.mp3?i=86.22812972256186', 'https://i62.servimg.com/u/f62/19/40/01/67/radiob12.jpg'],
                        ['Radio Blanik Cz', 'http://ice.abradio.cz/blanikcz128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiob12.jpg'],
			['Rádio BOHEMIA', 'http://88.99.38.244:8000/stream128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/bohemi10.jpg'],
                        ['Rádio Bonton', 'http://ice.actve.net/fm-bonton-128', 'https://i62.servimg.com/u/f62/19/40/01/67/radiob13.jpg'],
			['Rádio Chillout', 'http://mp3stream4.abradio.cz/chillout128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc12.jpg'],
			['Rádio Contact Liberec', 'http://icecast8.play.cz/contact128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc21.jpg'],
			['Rádio Country', 'http://mp3stream4.abradio.cz/country128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc14.jpg'],
			['Rádio Čas', 'http://icecast7.play.cz:8000/casradio128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc24.jpg'],
			['Rádio Čas Rock', 'http://icecast7.play.cz:8000/casrock128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc23.jpg'],
                        ['Rádio Dálnice', 'http://icecast8.play.cz/radiodalnice.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/radio-10.png'],
			['Rádio Dechovka', 'http://icecast5.play.cz:8000/dechovka128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiod13.jpg'],
			['Rádio Depeche Mode', 'http://mp3stream4.abradio.cz:8000/depeche128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiod11.jpg'],
			['Rádio Dixie', 'http://icecast8.play.cz/radiodixie192.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiod17.jpg'],
			['Radio Domino', 'http://mp3stream4.abradio.cz/domino128.mp3', 'https://i.servimg.com/u/f62/19/40/01/67/radiod14.jpg'],
                        ['Rádio Expert', 'http://mp3stream3.abradio.cz/expert-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioe10.jpg'],
			['Rádio Folk', 'http://mp3stream2.abradio.cz/folk128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiof15.jpg'],
			['Rádio Free 107 Fm', 'http://icecast8.play.cz/freeradio128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiof23.jpg'],
         		['Rádio G6', 'https://mpc.mediacp.eu:2000/stream/RadioG6', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_36.jpg'],
                        ['Rádio Golf', 'http://ice4.abradio.cz/golf128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiog11.jpg'],
			['Rádio Haná - Skyrock', 'http://icecast8.play.cz/skyrock128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios13.jpg'],
			['Rádio Haná', 'http://icecast8.play.cz/hana160.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh19.jpg'],
			['Rádio Humor', 'http://mp3stream4.abradio.cz:8000/humor128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh13.jpg'],
			['Rádio JIH', 'http://icecast6.play.cz/jih128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioj11.jpg'],
			['Rádio Jih - Cimbálka', 'http://icecast6.play.cz/jihcimbalka128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioj13.jpg'],
		       	['Rádio Kiss', 'http://icecast4.play.cz:8000/kiss128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok13.jpg'],
			['Rádio Krokodýl', 'http://icecast4.play.cz/krokodyl128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok11.jpg'],
			['Rádio Kroměříž', 'http://icecast6.play.cz/radio-kromeriz128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok12.jpg'],
		        ['Radio Like', 'https://node-30.zeno.fm/qffde4ffzmzuv?rj-ttl=5&rj-tok=AAABcQ0Vds0A0bakXrycnR4LTA', 'https://i.servimg.com/u/f46/19/40/01/67/radio_27.jpg'],
	        	['Radio Lovemusic', 'http://solid55.streamupsolutions.com:32053/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/lm_rad10.jpg'],
                        ['Rádio MB', 'http://icecast3.play.cz/radiomb.mp3', 'https://i.servimg.com/u/f46/19/40/01/67/radiom10.png'],
                        ['Rádio Merkur', 'http://ice4.abradio.cz/merkur-casino128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiom12.jpg'],
			['Rádio Nostalgie', 'http://icecast3.play.cz/radio-nostalgie128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radion13.jpg'],
			['Rádio Oldies Rock', 'http://mp3stream4.abradio.cz/oldiesrock128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioo10.jpg'],
		        ['Radio O.K.', 'https://node-10.zeno.fm/q7ura4u1akeuv?rj-ttl=5&rj-tok=AAABcQzZKFEAVyDUuNyclleYsg', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_25.jpg'],
		        ['Rádio Orlicko 95,5 FM', 'http://46.28.111.246/stream192.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/radioo10.jpg'],
         		['Rádio Ostravan', 'http://icecast9.play.cz/radio-ostravan-256.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/ostrav10.jpg'],
                        ['Rádio Pelhřimov', 'http://ca9.rcast.net:8054/', 'https://i.servimg.com/u/f46/19/40/01/67/rdio_p10.jpg'],
			['Rádio Pohádka', 'http://ice3.abradio.cz/pohadka128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop12.jpg'],
                        ['Rádio Povídka', 'http://ice.abradio.cz/povidka128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop11.jpg'],
        		['Rádio Play', 'http://hydra.shoutca.st:8271/play', 'https://i46.servimg.com/u/f46/19/40/01/67/radiop12.jpg'],
			['Rádio Ponte Records', 'http://ice3.abradio.cz:8000/ponterec128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiop15.jpg'],
		        ['Rádio Rubi', 'http://icecast8.play.cz/radiorubi128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior21.jpg'],
		        ['Radio R', 'http://radior.video.muni.cz:8000/FSS_mp3-128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_39.jpg'],
			['Rádio Samson FM', 'http://icecast8.play.cz/samsonfm128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios17.jpg'],
         		['Radio Sailor', 'https://node-26.zeno.fm/0wh8pvnyakeuv?rj-ttl=5&rj-tok=AAABdKyV0BgA4MI83O22J-L_Hg', 'https://i46.servimg.com/u/f46/19/40/01/67/rasdio10.jpg'],
			['Rádio Spin 96,2 FM', 'http://icecast4.play.cz/spin128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios14.jpg'],
		        ['Radio Svit', 'http://78.24.9.110:9490', 'https://i.servimg.com/u/f46/19/40/01/67/svit10.jpg'],
		        ['Radio SoundWave', 'http://81.91.84.138:8040', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_29.jpg'],
                        ['Radio Tloskov', 'http://ice3.abradio.cz/tloskov128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiot11.jpg'],
		    	['Rádio Zlín', 'http://212.111.2.151:8000/radiozlin_256.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioz11.jpg'],
                        ['Rádio Západ', 'http://icecast9.play.cz/radio-zapad-128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/zapad10.jpg'],
		        ['Rádio Z', 'https://ice.actve.net/fm-zet', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_38.jpg'],
		        ['Rebel Radio Brod', 'http://212.96.160.160:7988/;stream.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/rebel_10.jpg'],
			['Relaxace - Jedoucí Vlak', 'http://ice6.abradio.cz/relax-train128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior18.jpg'],
			['Relaxace - Letná bouřka', 'http://ice6.abradio.cz/relax-thunder-rain128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior20.jpg'],
			['Relaxace - Oheň v krbu', 'http://ice6.abradio.cz/relax-fire128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior21.jpg'],
			['Relaxace - Relaxace - Moře', 'http://ice6.abradio.cz/relax-sea128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior19.jpg'],
			['Relaxace - Zpěv ptákú', 'http://ice6.abradio.cz/relax-morning-birds128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior22.jpg'],
			['Rock Rádio', 'http://ice.abradio.cz:80/sumava128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior16.jpg'],
			['RockMax -Live', 'http://212.111.2.151:8000/rockmax_128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior15.jpg'],
			['RockZone 105,9', 'http://icecast2.play.cz/rockzone128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior22.jpg'],
			['Rocková zábava', 'http://ice.abradio.cz/rockzabava128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior10.jpg'],
			['SeeJay Rádio', 'http://mp3stream.abradio.cz:8000/seejay128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios11.jpg'],
			['Signál Rádio Brno', 'http://icecast3.play.cz/signal-brno192.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios15.jpg'],
			['Signál Rádio', 'http://icecast1.play.cz/signal128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios15.jpg'],
		        ['Svobodný vysílač CS', 'http://78.108.110.114:8000/live.opus', 'https://i46.servimg.com/u/f46/19/40/01/67/svobod11.jpg'],
        		['Svobodné Rádio', 'http://svobodneradio.radioca.st:8859/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/svobod12.jpg'],
			['This Is Radio', 'http://ice3.abradio.cz/this_is_radio.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiot10.jpg'],
         		['True Life in God Radio Czech', 'https://stream.galaxywebsolutions.com/proxy/tligradio_cs?mp=/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/tlig10.jpg'],
			['Undergroundradio', 'http://icecast2.play.cz/Underground128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/underg10.png'],
			['VPV rádio', 'http://88.99.38.244:8000/stream128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiov10.jpg'],
			['West Radio', 'https://node-16.zeno.fm/y6gyh7gg6heuv?rj-ttl=5&rj-tok=AAABcQ1G1YUAMgmz_r2kci4pLg', 'https://i46.servimg.com/u/f46/19/40/01/67/west-r10.jpg'],
        	       #['ZFK radio', 'https://node-14.zeno.fm/ere0xqyp5tzuv?rj-ttl=5&rj-tok=AAABdLZ6x3IA9OoWzVY9uWV6mg', 'https://i46.servimg.com/u/f46/19/40/01/67/c17544.png'],# deprecated
			['Známka Punku', 'http://ice.abradio.cz/znamkapunku128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/znamen10.png'],
			]
        
        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?cz_' + str(i), listitem=listItem, isFolder=True)
                i = i + 1
            xbmcplugin.endOfDirectory(int(sys.argv[1]))
            
        else:
        
            Title = list[int(self.opt2)][0]
            Icon = list[int(self.opt2)][2]
            URL = list[int(self.opt2)][1]
            
            import radioPlayer as player
            player.Main().start(Title, Icon, URL)
            
=======

        def test(self, selfGet):
            listitem = xbmcgui.ListItem()
            listitem.setArt({'fanart': __addonpath__ + '//' + 'fanart.jpg'})
            listitem.setProperty("IsPlayable", "true")
            if self.opt2 == '':
                i = 0

                for element in data['stanice']:
                    listitem.setLabel(element['nazov'])
                    listitem.setArt({'clearLogo': element['url']})
                    listitem.setArt({'icon': element['img']})
                    listitem.setArt({'poster': element['img']})  # for KODI < MATRIX
                    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?cz_' + str(i),
                                                listitem=listitem, isFolder=True)
                    i = i + 1
                xbmcplugin.endOfDirectory(int(sys.argv[1]))

            else:

                Title = data['stanice'][int(self.opt2)]['nazov']
                Icon = data['stanice'][int(self.opt2)]['img']
                URL = data['stanice'][int(self.opt2)]['url']

                import radioPlayer as player
                player.Main().start(Title, Icon, URL)

        url = apiUrl.apiUrl + 'getCZ'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            data = values
            test(self, selfGet)
        except requests.exceptions.RequestException as e:
            dialog = xbmcgui.Dialog()
            ok = dialog.ok(__addonname__, __addon__.getLocalizedString(30022))
>>>>>>> Stashed changes
