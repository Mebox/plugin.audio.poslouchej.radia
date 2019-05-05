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
            ['RMF FM', 'http://rmfon.pl/n/rmffm.pls', 'https://i62.servimg.com/u/f62/19/40/01/67/radior17.jpg'],
            ['RMF Classic rock', 'http://rmfon.pl/n/rmfclassicrock.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17558.png'],
            ['RMF Dance', 'http://rmfon.pl/n/rmfdance.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17551.png'],
            ['RMF R&B', 'http://rmfon.pl/n/rmfrnb.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png'],
            ['RMF MAXXX', 'http://rmfon.pl/n/rmfmaxxx.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17598.png'],
            ['RMF Classic', 'http://rmfon.pl/n/rmfclassic.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17552.png'],
            ['RMF Poplista', 'http://rmfon.pl/n/rmfpoplista.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17588.png'],
            ['RMF Polskie przeboje', 'http://rmfon.pl/n/rmfpprzeboje.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17599.png'],
            ['RMF Chillout', 'http://rmfon.pl/n/rmfchillout.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c175100.png'],
            ['RMF Bravo', 'http://rmfon.pl/n/rmfbravo.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c175101.png'],
            ['RMF LOVE', 'http://rmfon.pl/n/rmflove.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17557.png'],
            ['RMF Gold', 'http://rmfon.pl/n/rmfgold.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c175102.png'],
            ['RMF Smooth jazz', 'http://rmfon.pl/n/rmfsmoothjazz.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c175103.png'],
            ['RMF Swieta', 'http://rmfon.pl/n/rmfswieta.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17545.png'],
            ['RMF Przeboj roku', 'http://rmfon.pl/n/rmfprzebojroku.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png'],
            ['RMF MAXXX Hop bec', 'http://rmfon.pl/n/rmfhopbec.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png'],
            ['RMF Party', 'http://rmfon.pl/n/rmfparty.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png'],
            ['RMF Hot new', 'http://rmfon.pl/n/rmfhotnew.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17589.png'],
            ['RMF Alternatywa', 'http://rmfon.pl/n/rmfalternatywa.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17586.png'],
            ['RMF Club', 'http://rmfon.pl/n/rmfclub.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c175105.png'],
            ['RMF Lady Pank', 'http://rmfon.pl/n/rmfladypank.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png'],
            ['RMF Depeche Mode', 'http://rmfon.pl/n/rmfdepechemode.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17548.png'],
            ['RMF Polski rock', 'http://rmfon.pl/n/rmfpolskirock.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c175106.png'],
            ['RMF Hip hop', 'http://rmfon.pl/n/rmfhiphop.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png'],
            ['RMF PRL', 'http://rmfon.pl/n/rmfprl.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png'],
            ['RMF Blues', 'http://rmfon.pl/n/rmfblues.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17547.png'],
            ['RMF 50s', 'http://rmfon.pl/n/rmf50s.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17553.png'],
            ['RMF 60s', 'http://rmfon.pl/n/rmf60s.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17549.png'],
            ['RMF 70s', 'http://rmfon.pl/n/rmf70s.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c175108.png'],
            ['RMF 80s', 'http://rmfon.pl/n/rmf80s.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c175104.png'],
            ['RMF 90s', 'http://rmfon.pl/n/rmf90s.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c175110.png'],
            ['RMF Szanty', 'http://rmfon.pl/n/rmfszanty.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c175111.png'],
            ['RMF Polski hip hop', 'http://rmfon.pl/n/rmfpolskihiphop.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png'],
            ['RMF Cuba', 'http://rmfon.pl/n/rmfcuba.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17546.png'],
            ['RMF Francais', 'http://rmfon.pl/n/rmffrancais.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c175112.png'],
            ['RMF Queen', 'http://rmfon.pl/n/rmfqueen.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17550.png'],
            ['RMF Piosenka literacka', 'http://miastomuzyki.pl/n/rmfpiosenkaliteracka.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c175113.png'],
            ['RMF Celtic', 'http://rmfon.pl/n/rmfceltic.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c175114.png'],
            ['RMF Grunge', 'http://rmfon.pl/n/rmfgrunge.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c175115.png'],
            ['RMF Michael Jackson', 'http://miastomuzyki.pl/n/rmfmichaeljackson.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17554.png'],
            ['RMF Beatlemania', 'http://rmfon.pl/n/rmfbeatlemania.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17555.png'],
            ['RMF Styl', 'http://rmfon.pl/n/rmfstyl.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png'],
            ['RMF 2000', 'http://rmfon.pl/n/rmf2000.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c175116.png'],
            ['RMF 20 lat RMF FM', 'http://rmfon.pl/n/rmf20lat.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png'],
            ['RMF Chopin', 'http://rmfon.pl/n/rmfchopin.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png'],
            ['RMF Nostalgia', 'http://rmfon.pl/n/rmfnostalgia.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png'],
            ['RMF 2', 'http://rmfon.pl/n/rmf2.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png'],
            ['RMF 3', 'http://rmfon.pl/n/rmf3.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png'],
            ['RMF 4', 'http://rmfon.pl/n/rmf4.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png'],
            ['RMF 5', 'http://rmfon.pl/n/rmf5.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png'],
            ['RMF 70s disco', 'http://rmfon.pl/n/rmf70sdisco.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png'],
            ['RMF 80s disco', 'http://rmfon.pl/n/rmf80sdisco.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c175109.png'],
            ['RMF Niezapomniane melodie', 'http://rmfon.pl/n/rmfniezapomnianemelodie.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png'],
            ['RMF Best of RMFON', 'http://rmfon.pl/n/bestofrmfon.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png'],
            ['RMF w pracy', 'http://rmfon.pl/n/rmfwpracy.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png'],
            ['RMF Relaks', 'http://rmfon.pl/n/rmfrelaks.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png'],
            ['RMF Fitness', 'http://rmfon.pl/n/rmffitness.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png'],
            ['RMF Fitness rock', 'http://rmfon.pl/n/rmffitnessrock.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png'],
            ['RMF Top 5 dance', 'http://rmfon.pl/n/rmftop5dance.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png'],
            ['RMF Top 5 pl', 'http://rmfon.pl/n/rmftop5pl.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png'],
            ['RMF Top 5 pop', 'http://rmfon.pl/n/rmftop5pop.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png'],
            ['RMF Top 5 R&B', 'http://rmfon.pl/n/rmftop5rnb.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png'],
            ['RMF 90s dance', 'http://rmfon.pl/n/rmf90sdance.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png'],
            ['RMF Tekaciory', 'http://rmfon.pl/n/rmfteksciory.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png'],
            ['RMF Muzyka filmowa', 'http://rmfon.pl/n/rmffilmowa.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png'],
            ['RMF Radiofonia', 'http://rmfon.pl/n/radiofonia.pls', 'https://i46.servimg.com/u/f46/19/40/01/67/c17587.png']
            ]

        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?pl_' + str(i), listitem=listItem, isFolder=True)
                i = i + 1
            xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
        else:
                    
            opener = urllib2.build_opener()
            pageRadioPLS = opener.open(list[int(self.opt2)][1]).read()
            
            matchesIP = re.compile('(http://[^\s]+)\s').findall(pageRadioPLS)
                
            Title = list[int(self.opt2)][0]
            Icon = list[int(self.opt2)][2]
            URL = matchesIP[0]
        
            import radioPlayer as player
            player.Main().start(Title, Icon, URL)
            
