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
            ['1 HITS 80s', 'http://makri.cdnstream.com/1898_128', 'https://i46.servimg.com/u/f46/19/40/01/67/1_hits10.jpg'],
            ['80s80s Italo Disco', 'https://streams.80s80s.de/italohits/mp3-192/radiode/', 'https://i46.servimg.com/u/f46/19/40/01/67/c17585.png'],
            ['80s80s David Bowie', 'http://streams.80s80s.de/davidbowie/mp3-128/surfmusik', 'https://i62.servimg.com/u/f62/19/40/01/67/80bowi10.jpg'],
            ['80s80s Depeche Mode', 'http://streams.80s80s.de/dm/mp3-128/surfmusik', 'https://i62.servimg.com/u/f62/19/40/01/67/80mode10.jpg'],
            ['80s80s Love', 'http://streams.80s80s.de/love/mp3-128/surfmusik', 'https://i62.servimg.com/u/f62/19/40/01/67/80love10.jpg'],
            ['80s80s Prince', 'http://streams.80s80s.de/100/mp3-128/surfmusik', 'https://i62.servimg.com/u/f62/19/40/01/67/80prin10.jpg'],
            ['Antenne Bayern', 'http://mp3channels.webradio.antenne.de/antenne', 'https://i62.servimg.com/u/f62/19/40/01/67/antena10.jpg'],
            ['Antenne Bayern Weihnachtshits', 'http://mp3channels.webradio.antenne.de/weihnachts-hits', 'https://i62.servimg.com/u/f62/19/40/01/67/antena11.jpg'],
            ['Antenne Bayern Top 40', 'http://mp3channels.webradio.antenne.de/top-40', 'https://i62.servimg.com/u/f62/19/40/01/67/antena12.jpg'],
            ['Antenne Bayern 80er Kulthits', 'http://mp3channels.webradio.antenne.de/80er-kulthits', 'https://i62.servimg.com/u/f62/19/40/01/67/antena16.jpg'],
            ['Antenne Bayern 90er Hits', 'http://mp3channels.webradio.antenne.de/90er-hits', 'https://i62.servimg.com/u/f62/19/40/01/67/antena17.jpg'],
            ['Antenne Bayern Workout Hits', 'http://mp3channels.webradio.antenne.de/workout-hits', 'https://i62.servimg.com/u/f62/19/40/01/67/antenn10.jpg'],
            ['Antenne Bayern Lovesongs', 'http://mp3channels.webradio.antenne.de/lovesongs', 'https://i62.servimg.com/u/f62/19/40/01/67/f3c7d910.jpg'],
            ['Antenne Bayern Fresh', 'http://channels.webradio.antenne.de/fresh', 'https://i62.servimg.com/u/f62/19/40/01/67/antenn11.jpg'],
            ['Antenne Bayern Classic Rock', 'http://mp3channels.webradio.antenne.de/classic-rock-live', 'https://i62.servimg.com/u/f62/19/40/01/67/antenn13.jpg'],
            ['Antenne Bayern Oldies but Goldies', 'http://mp3channels.webradio.antenne.de/oldies-but-goldies', 'https://i62.servimg.com/u/f62/19/40/01/67/antena13.jpg'],
            ['Antenne Bayern Chillout', 'http://mp3channels.webradio.antenne.de/chillout', 'https://i62.servimg.com/u/f62/19/40/01/67/antena14.jpg'],
            ['Disco Party Radio', 'http://stream.laut.fm/-z-i-s-c-o-party-70s-80s', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_33.jpg'],
            ['FFH Digital', 'http://mp3.ffh.de/radioffh/hqlivestream.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/ffh_di10.jpg'],
            ['FFH Eurodance', 'http://mp3.ffh.de/ffhchannels/hqeurodance.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/ffh_di11.jpg'],
            ['FFH Top 40', 'http://mp3.ffh.de/ffhchannels/hqtop40.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/ffh_di12.jpg'],
            ['FFH Lounge', 'http://mp3.ffh.de/ffhchannels/hqlounge.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/ffh_di13.jpg'],
            ['FFH Brandneu', 'http://mp3.ffh.de/ffhchannels/hqbrandneu.aac', 'https://i62.servimg.com/u/f62/19/40/01/67/ffh_br10.jpg'],
            ['FFH - Die 80-er', 'http://mp3.ffh.de/ffhchannels/hq80er.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/ffh_di10.jpg'],
            ['FFH - Just 90s', 'http://mp3.ffh.de/ffhchannels/hq90er.aac', 'https://i11.servimg.com/u/f11/19/40/01/67/ffh_ju10.jpg'],
            ['M1.FM - Kuschelschlager', 'http://tuner.m1.fm/kuschelschlager.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/m1fm1810.png'],
            ['M1.FM - Charts', 'http://tuner.m1.fm/charts.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/charts10.jpg'],
            ['M1.FM - Hits', 'http://tuner.m1.fm/hits.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hits-c10.jpg'],
            ['M1.FM - Clubmix', 'http://tuner.m1.fm/clubmix.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/clubmi10.jpg'],
            ['M1.FM - Softpop', 'http://tuner.m1.fm/softpop.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/softpo10.jpg'],
            ['M1.FM - Chillout', 'http://tuner.m1.fm/chillout.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/chillo10.jpg'],
            ['M1.FM - Urban', 'http://tuner.m1.fm/urban.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/urban-10.jpg'],
            ['M1.FM - Rock', 'http://tuner.m1.fm/rock.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/rock-c10.jpg'],
            ['M1.FM - Schlagerparty', 'http://tuner.m1.fm/schlagerparty.mp3', 'https://i.servimg.com/u/f46/19/40/01/67/schlag10.jpg'],
            ['M1.FM - Oldies', 'http://tuner.m1.fm/oldies.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/oldies10.jpg'],
            ['M1.FM - 80ER', 'http://tuner.m1.fm/80er.mp3', 'https://i.servimg.com/u/f46/19/40/01/67/80er-c10.jpg'],
            ['M1.FM - 90ER', 'http://tuner.m1.fm/90er.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/90er-c10.jpg'],
            ['N-Joy', 'https://ndr-njoy-live.sslcast.addradio.de/ndr/njoy/live/mp3/128/stream.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/njoy10.jpg'],
            ['Radio On Disco', 'https://0n-disco.radionetz.de/0n-disco.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_32.jpg']

            ]

        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?ger_' + str(i), listitem=listItem, isFolder=True)
                i = i + 1
            xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
        else:
        
            Title = list[int(self.opt2)][0]
            Icon = list[int(self.opt2)][2]
            URL = list[int(self.opt2)][1]
        
            import radioPlayer as player
            player.Main().start(Title, Icon, URL)
            
