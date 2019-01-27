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
['Evropa 2', 'http://icecast3.play.cz/evropa2-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioe11.jpg'],
['Evropa 2 - Youradio HOT', 'http://ice.actve.net/web-e2-hot', 'https://i46.servimg.com/u/f46/19/40/01/67/europa11.jpg'],
['Evropa 2 - Youradio Top 40', 'http://ice.actve.net/web-e2-top40', 'https://i46.servimg.com/u/f46/19/40/01/67/europa12.jpg'],
['Evropa 2 - Youradio Movin', 'http://ice.actve.net/web-e2-movin', 'https://i46.servimg.com/u/f46/19/40/01/67/europa13.jpg'],
['Evropa 2 - Youradio Ceskoslovenske hity', 'http://ice.actve.net/web-e2-csweb', 'https://i46.servimg.com/u/f46/19/40/01/67/europa10.jpg'],
['Evropa 2 - Youradio Flashback', 'http://ice.actve.net/web-e2-flashback', 'https://i46.servimg.com/u/f46/19/40/01/67/europa14.jpg'],
['Frekvence1', 'http://icecast4.play.cz/frekvence1-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiof16.jpg'],
['Frekvence1 - Youradio Legendy', 'http://pool.cdn.lagardere.cz:80/web-f1-legendy', 'https://i62.servimg.com/u/f62/19/40/01/67/radiof19.jpg'],
['Frekvence1 - Youradio 80s', 'http://pool.cdn.lagardere.cz:80/web-80', 'https://i62.servimg.com/u/f62/19/40/01/67/radiof21.jpg'],
['Impuls Radio', 'http://icecast5.play.cz/impuls128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioi12.jpg'],
['Cesky Impuls', 'http://icecast6.play.cz:8000/cesky-impuls.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioi13.jpg'],
['Cesky rozhlas 1 - Radiozurnal', 'http://icecast7.play.cz:443/cro1-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior12.jpg'],
['Cesky rozhlas 2 - Praha', 'http://icecast7.play.cz:443/cro2-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc22.jpg'],
['Cesky rozhlas 3 - Vltava', 'http://icecast5.play.cz:8000/cro3-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc25.jpg'],
['CRo Regina DAB Praha', 'http://icecast2.play.cz:8000/croregina128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc32.jpg'],
['CRo Ceske Budejovice', 'http://icecast2.play.cz:8000/crocb128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc31.jpg'],
['CRo Hradec Kralove', 'http://icecast2.play.cz:8000/crohk128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc30.jpg'],
['CRo Ostrava', 'http://icecast2.play.cz:8000/croov128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc27.jpg'],
['CRo Brno', 'http://icecast2.play.cz:8000/crobrno128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc28.jpg'],
['CRo Olomouc', 'http://icecast2.play.cz:8000/crool128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc26.jpg'],
['CRo Pardubice', 'http://icecast2.play.cz:8000/cropardubice128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop19.jpg'],
['CRo Liberec', 'http://icecast2.play.cz:8000/croliberec128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiol10.jpg'],
['CRo Plzen', 'http://icecast2.play.cz:8000/croplzen128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/croplz12.png'],
['CRo Plzen studio Karlovy Vary', 'http://icecast2.play.cz:8000/crokv128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/croplz13.png'],
['CRo Region - Vysocina', 'http://icecast2.play.cz:8000/crovysocina128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/croreg10.png'],
['CRo Region Stredocesky kraj', 'http://icecast2.play.cz:8000/croregion128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiov12.jpg'],
['CRo Sever', 'http://icecast2.play.cz:8000/crosever128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios18.jpg'],
['CRo Wave', 'http://icecast5.play.cz:8000/crowave-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiow10.jpg'],
['CRo Jazz', 'http://icecast2.play.cz:8000/crojazz128aac', 'https://i62.servimg.com/u/f62/19/40/01/67/radioj14.jpg'],
['CRo D-dur', 'http://icecast5.play.cz:8000/croddur-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiod18.jpg'],
['CRo Plus', 'http://icecast1.play.cz:443/croplus128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop18.jpg'],
['CRo Radio Junior', 'http://icecast5.play.cz:8000/crojuniormaxi128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioj15.jpg'],
['Radio Junior Pisnicky', 'http://icecast7.play.cz:443/crojuniormini128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc29.jpg'],
['Radio Retro', 'http://icecast7.play.cz/croretro128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior13.jpg'],
['Radiozurnal – olympijsky special', 'http://icecast8.play.cz/crosport128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/crospo10.png'],
['Signal Radio', 'http://icecast1.play.cz/signal128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios15.jpg'],
['Signal Radio Brno', 'http://icecast3.play.cz/signal-brno192.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios15.jpg'],
['Radio Zlin', 'http://212.111.2.151:8000/radiozlin_256.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioz11.jpg'],
['COLOR Music Radio', 'http://icecast8.play.cz:443/color128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc19.jpg'],
['Proglas', 'http://icecast2.play.cz/proglas128', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop17.jpg'],
['Classic Praha', 'http://icecast8.play.cz/classic128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc34.jpg'],
['Be iN Radio Network', 'http://icecast1.play.cz/beinradionetwork1-128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/be-in-10.png'],
['E-Radio JAZZINEC', 'http://ice3.abradio.cz/jazzinec128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioj10.jpg'],
['HipHopVibes Radio', 'http://mp3stream4.abradio.cz/hiphopvibes128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh14.jpg'],
['VPV radio', 'http://88.99.38.244:8000/stream128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiov10.jpg'],
['Undergroundradio', 'http://icecast2.play.cz/Underground128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/underg10.png'],
['Radio Samson FM', 'http://icecast8.play.cz/samsonfm128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios17.jpg'],
['Radio 66', 'http://ice3.abradio.cz/route128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radio610.jpg'],
['Radio Country', 'http://mp3stream4.abradio.cz/country128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc14.jpg'],
['Radio Folk', 'http://mp3stream2.abradio.cz/folk128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiof15.jpg'],
['Radio Humor', 'http://mp3stream4.abradio.cz:8000/humor128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh13.jpg'],
['Radio Povidka', 'http://ice.abradio.cz/povidka128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop11.jpg'],
['Radio Pohadka', 'http://ice3.abradio.cz/pohadka128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop12.jpg'],
['Pigy.cz – Pohadky', 'http://pool.cdn.lagardere.cz/web-pg-pohadky', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop10.jpg'],
['Cimrmanovo radio', 'http://liquiddoom.net:8000/cimrman', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc20.jpg'],
['Radio Dechovka', 'http://icecast5.play.cz:8000/dechovka128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiod13.jpg'],
['Oldies radio', 'http://ice.abradio.cz/oldiesradio128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioo12.jpg'],
['Radio Nostalgie', 'http://icecast3.play.cz/radio-nostalgie128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radion13.jpg'],
['Radio Benesov City', 'http://ice6.abradio.cz/benesov128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/beneso10.png'],
['Radio Dalnice', 'http://icecast8.play.cz/radiodalnice.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/radio-10.png'],
['Radio Petrov', 'http://icecast6.play.cz:8000/petrov128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop14.jpg'],
['Radio Petrov Rock', 'http://play.radiopetrov.com:8000/petrovR', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop14.jpg'],
['Radio Petrov Folk', 'http://play.radiopetrov.com:8000/petrovFC', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop14.jpg'],
['Country Radio', 'http://icecast4.play.cz:443/country128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc33.jpg'],
['Radio Dixie', 'http://icecast6.play.cz/radiodixie192.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiod17.jpg'],
['Radio Kiss', 'http://icecast4.play.cz:8000/kiss128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok13.jpg'],
['Radio Rubi', 'http://icecast8.play.cz/radiorubi128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior21.jpg'],
['Radio Contact Liberec', 'http://icecast8.play.cz/contact128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc21.jpg'],
['Radio Kromeriz', 'http://icecast6.play.cz/radio-kromeriz128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok12.jpg'],
['Radio JIH', 'http://icecast6.play.cz/jih128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioj11.jpg'],
['Radio Jih – Cimbalka', 'http://icecast6.play.cz/jihcimbalka128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioj13.jpg'],
['Radio Krokodyl', 'http://icecast4.play.cz/krokodyl128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok11.jpg'],
['Radio Bonton', 'http://pool.cdn.lagardere.cz/fm-bonton-128', 'https://i62.servimg.com/u/f62/19/40/01/67/radiob13.jpg'],
['Radio Tloskov', 'http://ice3.abradio.cz/tloskov128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiot11.jpg'],
['COOP TIP Radio', 'http://ice4.abradio.cz/coop128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc16.jpg'],
['Coop TUTY Radio', 'http://ice4.abradio.cz/cooptuty128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/tuty10.png'],
['Radio Merkur', 'http://ice4.abradio.cz/merkur-casino128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiom12.jpg'],
['Radio Expert', 'http://mp3stream3.abradio.cz/expert-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioe10.jpg'],
['DAB Plus Top 40', 'http://icecast6.play.cz/dabplus-top40.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiod12.jpg'],
['Fajn Radio', 'http://ice.abradio.cz/fajn128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiof13.jpg'],
['Fajn Radio Fresh', 'http://ice.abradio.cz/fajnfresh128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiof12.jpg'],
['Fajn Party', 'http://ice.abradio.cz/fajnparty128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/fan_pa10.png'],
['Radio Golf', 'http://ice4.abradio.cz/golf128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiog11.jpg'],
['Radio Blanik', 'http://ice.abradio.cz/blanikfm128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiob12.jpg'],
['Radio Blanik Cz', 'http://ice.abradio.cz/blanikcz128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiob12.jpg'],
['Hitradio City', 'http://ice.abradio.cz/cityfm128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc37.jpg'],
['Hitradio City Osmdesatka', 'http://ice.abradio.cz/city80128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh12.jpg'],
['Hitradio City Devadesatka', 'http://ice.abradio.cz:8000/city90128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh16.jpg'],
['Radio City milenium', 'http://ice.abradio.cz/citymi128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh17.jpg'],
['Hitradio City Zona lasky', 'http://ice.abradio.cz/cityzl128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh18.jpg'],
['Hitradio PopRock', 'http://ice.abradio.cz/hitpoprock128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh11.jpg'],
['Hitradio Zona lasky', 'http://ice.abradio.cz/hitzl128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh11.jpg'],
['Hitradio Osmdesatka', 'http://ice.abradio.cz/hit80128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh11.jpg'],
['Hitradio Devadesatka', 'http://ice.abradio.cz/hit90128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh11.jpg'],
['Hitradio Cerna Hora', 'http://ice.abradio.cz/cernahora128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitrad16.jpg'],
['Hitradio Magic', 'http://ice.abradio.cz/magic128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitrad12.jpg'],
['Hitradio Orion', 'http://ice.abradio.cz/orion128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitcit12.jpg'],
['Hitradio Vysocina', 'http://ice5.abradio.cz/hitvysocina128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitcit13.jpg'],
['Hitradio Dragon', 'http://ice.abradio.cz/dragon128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitcit11.jpg'],
['Hitradio City', 'http://ice.abradio.cz/citybrno128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitcit10.jpg'],
['Hitradio Faktor', 'http://ice.abradio.cz/faktor128a.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitrad13.jpg'],
['Hitradio FM', 'http://ice.abradio.cz/hitradiofm128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitrad15.jpg'],
['Hitradio FM Plus', 'http://ice.abradio.cz/fmplus128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitrad14.jpg'],
['Radio Madonna', 'http://mp3stream4.abradio.cz:8000/madonna128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiom11.jpg'],
['Radio Depeche Mode', 'http://mp3stream4.abradio.cz:8000/depeche128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiod11.jpg'],
['Radio Olympic', 'http://ice.abradio.cz/olympic128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioo11.jpg'],
['Radio Radnice', 'http://ice3.abradio.cz/radnice128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior11.jpg'],
['Expres FM', 'http://icecast8.play.cz/expres128mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/expres10.png'],
['Club Radio', 'http://icecast2.play.cz:8000/Clubradio.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc18.jpg'],
['Radio Free 107 Fm', 'http://icecast8.play.cz/freeradio128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiof23.jpg'],
['Radio Spin 96,2 FM', 'http://icecast4.play.cz/spin128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios14.jpg'],
['Dance Radio', 'http://pool.cdn.lagardere.cz/dance-radio128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiod10.jpg'],
['SeeJay Radio', 'http://mp3stream.abradio.cz:8000/seejay128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios11.jpg'],
['Radio Chillout', 'http://mp3stream4.abradio.cz/chillout128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc12.jpg'],
['Clubbeat Radio', 'http://mp3stream4.abradio.cz/clubbeat128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc11.jpg'],
['This Is Radio', 'http://ice3.abradio.cz/this_is_radio.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiot10.jpg'],
['Drumandbass Radio SHADOWBOX', 'http://ice3.abradio.cz/shadowbox128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios10.jpg'],
['Dance Club Radio', 'http://mp3stream4.abradio.cz/dance128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/dancec11.jpg'],
['Helax 93,7', 'http://ice.abradio.cz:8000/helax128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh10.jpg'],
['HEY Radio', 'http://icecast3.play.cz/hey-radio128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh20.jpg'],
['Radio Hana', 'http://icecast8.play.cz/hana160.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh19.jpg'],
['Radio Hana - Skyrock', 'http://icecast8.play.cz/skyrock128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios13.jpg'],
['Radio Cas (Brno)', 'http://icecast7.play.cz:8000/casbrno128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc24.jpg'],
['Radio Cas (Ostrava)', 'http://icecast7.play.cz:8000/casradio128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc24.jpg'],
['Radio Cas Rock', 'http://icecast7.play.cz:8000/casrock128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc23.jpg'],
['Cas Rock NATVRDO', 'http://icecast8.play.cz/rocknatvrdo.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/cas_ro10.png'],
['Radio Beat', 'http://ice6.abradio.cz/beat128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/beat10.png'],
['RockZone 105,9', 'http://icecast2.play.cz/rockzone128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior22.jpg'],
['Radio Best of Rock', 'http://mp3stream4.abradio.cz/bestofrock128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiob10.jpg'],
['Metalomanie', 'http://ice.abradio.cz/metalomanie128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/metalm10.jpg'],
['Rocková zabava', 'http://ice.abradio.cz/rockzabava128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior10.jpg'],
['Radio Oldies Rock', 'http://mp3stream4.abradio.cz/oldiesrock128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioo10.jpg'],
['Alternative Times Radio', 'http://ice3.abradio.cz/alternative128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioa10.jpg'],
['WebRadio Epigon', 'http://mp3stream3.abradio.cz/epigon128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radioe16.jpg'],
['Radio Ponte Records', 'http://ice3.abradio.cz:8000/ponterec128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiop15.jpg'],
['Znamka Punku', 'http://ice.abradio.cz/znamkapunku128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/znamen10.png'],
['RockMax Radio', 'http://212.111.2.151:8000/rockmax_256.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior15.jpg'],
['RockMax Radio Oldies', 'http://212.111.2.151:8000/rm_old_256.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior15.jpg'],
['RockMax Radio Heavy', 'http://212.111.2.151:8000/rm_hard_256.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior15.jpg'],
['Rock Radio', 'http://ice.abradio.cz:80/sumava128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior16.jpg'],
['Radio Oldies Rock', 'http://mp3stream4.abradio.cz/oldiesrock128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior16.jpg'],
['Metal Heart Radio', 'http://fr.radio-streamhosting.com:8000/metalheartradio128mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/metal_10.jpg'],
['Koule.cz Filmove Melodie', 'http://ice-01.lagardere.cz:80/web-rb-melodie', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok14.jpg'],
['Radio BOHEMIA', 'http://88.99.38.244:8000/stream128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/bohemi10.jpg'],
['Relaxace - Jedouci Vlak', 'http://ice6.abradio.cz/relax-train128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior18.jpg'],
['Relaxace - Relaxace - More', 'http://ice6.abradio.cz/relax-sea128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior19.jpg'],
['Relaxace - Letni bourka', 'http://ice6.abradio.cz/relax-thunder-rain128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior20.jpg'],
['Relaxace - Ohen v krbu', 'http://ice6.abradio.cz/relax-fire128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior21.jpg'],
['Relaxace - Zpev ptaku', 'http://ice6.abradio.cz/relax-morning-birds128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior22.jpg']
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
            