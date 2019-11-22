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
            ['Alternative Times Radio', 'http://ice3.abradio.cz/alternative128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioa10.jpg'],
			['Be iN Radio Network', 'http://icecast1.play.cz/beinradionetwork1-128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/be-in-10.png'],
			['Classic Praha', 'http://icecast8.play.cz/classic128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc34.jpg'],
			['Club Rádio', 'http://icecast2.play.cz:8000/Clubradio.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc18.jpg'],
			['Clubbeat Rádio', 'http://mp3stream4.abradio.cz/clubbeat128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc11.jpg'],
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
                        ['Český Rozhlas Rádio Retro', 'http://icecast7.play.cz/croretro128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior13.jpg'],
                        ['Český Rozhlas Radiožurnál Sport', 'http://icecast8.play.cz/crosport128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/crospo11.png'],
                        ['DAB Plus Top 40', 'http://icecast6.play.cz/dabplus-top40.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiod12.jpg'],
                        ['Dance Club Rádio', 'http://mp3stream4.abradio.cz/dance128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/dancec11.jpg'],
			['Dance Rádio', 'http://icecast6.play.cz/dance-radio320.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiod10.jpg'],
			['Drumandbass Radio SHADOWBOX', 'http://ice3.abradio.cz/shadowbox128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios10.jpg'],
			['E-Radio JAZZINEC', 'http://ice3.abradio.cz/jazzinec128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioj10.jpg'],
			['Evropa 2', 'http://icecast3.play.cz/evropa2-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioe11.jpg'],
                        ['Evropa 2 - Youradio HOT', 'http://ice.actve.net/web-e2-hot', 'https://i46.servimg.com/u/f46/19/40/01/67/europa11.jpg'],
                        ['Evropa 2 - Youradio Top 40', 'http://ice.actve.net/web-e2-top40', 'https://i46.servimg.com/u/f46/19/40/01/67/europa12.jpg'],
                        ['Evropa 2 - Youradio Movin', 'http://ice.actve.net/web-e2-movin', 'https://i46.servimg.com/u/f46/19/40/01/67/europa13.jpg'],
                        ['Evropa 2 - Youradio Československé hity', 'http://ice.actve.net/web-e2-csweb', 'https://i46.servimg.com/u/f46/19/40/01/67/europa10.jpg'],
                        ['Evropa 2 - Youradio Flashback', 'http://ice.actve.net/web-e2-flashback', 'https://i46.servimg.com/u/f46/19/40/01/67/europa14.jpg'],
			['Expres FM', 'http://icecast8.play.cz/expres128mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/expres10.png'],
                        ['Fajn Radio', 'http://ice.abradio.cz/fajn128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiof13.jpg'],
                        ['Fajn Radio Fresh', 'http://ice.abradio.cz/fajnfresh128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiof12.jpg'],
                        ['Fajn Party', 'http://ice.abradio.cz/fajnparty128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/fan_pa10.png'],
			['Frekvence 1', 'http://icecast4.play.cz/frekvence1-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiof16.jpg'],
			['Frekvence 1 - Youradio Legendy', 'http://ice.actve.net/web-f1-legendy', 'https://i46.servimg.com/u/f46/19/40/01/67/f1_leg10.jpg'],
			['Frekvence 1 - Youradio 80s', 'http://ice.actve.net/web-80', 'https://i62.servimg.com/u/f62/19/40/01/67/radiof21.jpg'],
			['HEY Radio', 'http://icecast3.play.cz/hey-radio128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh20.jpg'],
			['Helax 93,7', 'http://ice.abradio.cz:8000/helax128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh10.jpg'],
			['HipHopVibes Rádio', 'http://mp3stream4.abradio.cz/hiphopvibes128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh14.jpg'],
			['Hitrádio FM Plus', 'http://ice.abradio.cz/fmplus128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitrad14.jpg'],
			['Hitrádio FM', 'http://ice.abradio.cz/hitradiofm128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitrad15.jpg'],
			['Hitrádio Faktor', 'http://ice.abradio.cz/faktor128a.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitrad13.jpg'],
			['Hitrádio Magic', 'http://ice.abradio.cz/magic128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitrad12.jpg'],
                        ['Hitrádio City', 'http://ice.abradio.cz/citybrno128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitcit10.jpg'],
			['Hitrádio City Zóna lásky', 'http://ice.abradio.cz/cityzl128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh18.jpg'],
			['Hitrádio PopRock', 'http://ice.abradio.cz/hitpoprock128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh11.jpg'],
			['Hitrádio Osmdesátka', 'http://ice.abradio.cz/hit80128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh11.jpg'],
			['Hitrádio Devadesátka', 'http://ice.abradio.cz/hit90128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh11.jpg'],
                        ['Radio City milenium', 'http://ice.abradio.cz/citymi128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh17.jpg'],
			['Hitrádio Černá Hora', 'http://ice.abradio.cz/cernahora128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitrad16.jpg'],
			['Hitrádio Orion', 'http://ice.abradio.cz/orion128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitcit12.jpg'],
			['Hitrádio Vysočina', 'http://ice5.abradio.cz/hitvysocina128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitcit13.jpg'],
			['Hitrádio Dragon', 'http://ice.abradio.cz/dragon128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitcit11.jpg'],
			['Impuls Rádio', 'http://icecast5.play.cz/impuls128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioi12.jpg'],
                        ['Impuls - Český Impuls', 'http://icecast6.play.cz:8000/cesky-impuls.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioi13.jpg'],
			['Koule.cz Filmové Melodie', 'http://ice.actve.net/web-rb-melodie', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok14.jpg'],
		        ['Metal Heart Rádio', 'http://fr.radio-streamhosting.com:8000/metalheartradio128mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/metal_10.jpg'],
			['Metalomanie', 'http://ice.abradio.cz/metalomanie128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/metalm10.jpg'],
			['Oldies rádio', 'http://ice.abradio.cz/oldiesradio128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioo12.jpg'],
			['Pigy.cz - Disko Trysko', 'http://ice.actve.net/web-pg-disko', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop10.jpg'],
			['Pigy.cz - Písničky z Pohádek', 'http://ice.actve.net/web-pg-pisnicky', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop10.jpg'],
			['Pigy.cz - Pohádky', 'http://ice.actve.net/web-pg-pohadky', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop10.jpg'],
			['Proglas', 'http://icecast2.play.cz/proglas128', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop17.jpg'],
			['Rádio Benešov City', 'http://ice6.abradio.cz/benesov128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/beneso10.png'],
			['Rádio Best of Rock', 'http://mp3stream4.abradio.cz/bestofrock128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiob10.jpg'],
			['Rádio Beat', 'http://ice6.abradio.cz/beat128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/beat10.png'],
			['Rádio Best of Rock', 'http://mp3stream4.abradio.cz/bestofrock128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiob10.jpg'],
			['Rádio Blaník', 'http://ice.abradio.cz/blanikfm128.mp3?i=86.22812972256186', 'https://i62.servimg.com/u/f62/19/40/01/67/radiob12.jpg'],
                        ['Radio Blanik Cz', 'http://ice.abradio.cz/blanikcz128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiob12.jpg'],
			['Rádio BOHEMIA', 'http://88.99.38.244:8000/stream128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/bohemi10.jpg'],
                        ['Rádio Bonton', 'http://icecast3.play.cz/bonton-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiob13.jpg'],
			['Rádio Chillout', 'http://mp3stream4.abradio.cz/chillout128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc12.jpg'],
			['Rádio Contact Liberec', 'http://icecast8.play.cz/contact128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc21.jpg'],
			['Rádio Country', 'http://mp3stream4.abradio.cz/country128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc14.jpg'],
                        ['Rádio Čas (Brno)', 'http://icecast7.play.cz:8000/casbrno128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc24.jpg'],
			['Rádio Čas (Ostrava)', 'http://icecast7.play.cz:8000/casradio128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc24.jpg'],
			['Rádio Čas Rock', 'http://icecast7.play.cz:8000/casrock128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc23.jpg'],
                        ['Rádio Čas Rock NATVRDO', 'http://icecast8.play.cz/rocknatvrdo.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/cas_ro10.png'],
			['Rádio Dechovka', 'http://icecast5.play.cz:8000/dechovka128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiod13.jpg'],
			['Rádio Depeche Mode', 'http://mp3stream4.abradio.cz:8000/depeche128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiod11.jpg'],
			['Rádio Dixie', 'http://icecast6.play.cz/radiodixie192.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiod17.jpg'],
			['Rádio Dálnice', 'http://icecast8.play.cz/radiodalnice.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/radio-10.png'],
                        ['Rádio Expert', 'http://mp3stream3.abradio.cz/expert-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioe10.jpg'],
			['Rádio Folk', 'http://mp3stream2.abradio.cz/folk128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiof15.jpg'],
			['Rádio Free 107 Fm', 'http://icecast8.play.cz/freeradio128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiof23.jpg'],
                        ['Rádio Golf', 'http://ice4.abradio.cz/golf128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiog11.jpg'],
			['Rádio Haná - Skyrock', 'http://icecast8.play.cz/skyrock128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios13.jpg'],
			['Rádio Haná', 'http://icecast8.play.cz/hana160.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh19.jpg'],
			['Rádio Humor', 'http://mp3stream4.abradio.cz:8000/humor128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh13.jpg'],
			['Rádio JIH', 'http://icecast6.play.cz/jih128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioj11.jpg'],
			['Rádio Jih - Cimbálka', 'http://icecast6.play.cz/jihcimbalka128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioj13.jpg'],
			['Rádio Kiss', 'http://icecast4.play.cz:8000/kiss128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok13.jpg'],
			['Rádio Krokodýl', 'http://icecast4.play.cz/krokodyl128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok11.jpg'],
			['Rádio Kroměříž', 'http://icecast6.play.cz/radio-kromeriz128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok12.jpg'],
			['Rádio Madonna', 'http://mp3stream4.abradio.cz:8000/madonna128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiom11.jpg'],
                        ['Rádio Merkur', 'http://ice4.abradio.cz/merkur-casino128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiom12.jpg'],
			['Rádio Nostalgie', 'http://icecast3.play.cz/radio-nostalgie128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radion13.jpg'],
			['Rádio Oldies Rock', 'http://mp3stream4.abradio.cz/oldiesrock128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioo10.jpg'],
		        ['Rádio Orlicko 95,5 FM', 'http://46.28.111.246/stream192.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/radioo10.jpg'],
		        ['Rádio Patriot', 'http://ice3.abradio.cz/patriot128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/patrio10.jpg'],
                        ['Rádio Petrov', 'http://icecast6.play.cz:8000/petrov128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop14.jpg'],
			['Rádio Pohádka', 'http://ice3.abradio.cz/pohadka128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop12.jpg'],
                        ['Rádio Povídka', 'http://ice.abradio.cz/povidka128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop11.jpg'],
			['Rádio Ponte Records', 'http://ice3.abradio.cz:8000/ponterec128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiop15.jpg'],
		        ['Rádio Rubi', 'http://icecast8.play.cz/radiorubi128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior21.jpg'],
			['Rádio Samson FM', 'http://icecast8.play.cz/samsonfm128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios17.jpg'],
			['Rádio Spin 96,2 FM', 'http://icecast4.play.cz/spin128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios14.jpg'],
		        ['Rádio Svit Zlín', 'http://stream1.goq.cz:8001/radio-svit-zlin', 'https://i46.servimg.com/u/f46/19/40/01/67/svit10.jpg'],
                        ['Radio Tloskov', 'http://ice3.abradio.cz/tloskov128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiot11.jpg'],
			['Rádio Zlín', 'http://212.111.2.151:8000/radiozlin_256.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioz11.jpg'],
		        ['Rebel Radio Brod', 'http://212.96.160.160:7988/;stream.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/rebel_10.jpg'],
			['Relaxace - Jedoucí Vlak', 'http://ice6.abradio.cz/relax-train128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior18.jpg'],
			['Relaxace - Letná bouřka', 'http://ice6.abradio.cz/relax-thunder-rain128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior20.jpg'],
			['Relaxace - Oheň v krbu', 'http://ice6.abradio.cz/relax-fire128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior21.jpg'],
			['Relaxace - Relaxace - Moře', 'http://ice6.abradio.cz/relax-sea128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior19.jpg'],
			['Relaxace - Zpěv ptákú', 'http://ice6.abradio.cz/relax-morning-birds128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior22.jpg'],
			['Rock Rádio', 'http://ice.abradio.cz:80/sumava128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior16.jpg'],
			['RockMax -Live', 'http://212.111.2.151:8000/rockmax_128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior15.jpg'],
		        ['RockMax-Hard', 'http://212.111.2.151:8000/rm_hard_256.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior15.jpg'],
			['RockMax-Oldies', 'http://212.111.2.151:8000/rm_old_256.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior15.jpg'],
			['RockMax-Blue', 'http://212.111.2.151:8000/rm_blue_128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior15.jpg'],
			['RockZone 105,9', 'http://icecast2.play.cz/rockzone128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior22.jpg'],
			['Rocková zábava', 'http://ice.abradio.cz/rockzabava128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior10.jpg'],
			['SeeJay Rádio', 'http://mp3stream.abradio.cz:8000/seejay128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios11.jpg'],
			['Signál Rádio Brno', 'http://icecast3.play.cz/signal-brno192.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios15.jpg'],
			['Signál Rádio', 'http://icecast1.play.cz/signal128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios15.jpg'],
			['This Is Radio', 'http://ice3.abradio.cz/this_is_radio.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiot10.jpg'],
			['Undergroundradio', 'http://icecast2.play.cz/Underground128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/underg10.png'],
			['VPV rádio', 'http://88.99.38.244:8000/stream128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiov10.jpg'],
			['WebRádio Epigon', 'http://mp3stream3.abradio.cz/epigon128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radioe16.jpg'],
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
            
