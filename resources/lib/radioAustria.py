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
            ['ANTENNE VORARLBERG', 'http://webradio.antennevorarlberg.at/live', 'https://i46.servimg.com/u/f46/19/40/01/67/c17518.png'],
            ['ANTENNE VORARLBERG 80er Hits', 'http://webradio.antennevorarlberg.at/80er', 'https://i46.servimg.com/u/f46/19/40/01/67/c17514.png'],
            ['ANTENNE VORARLBERG Hits', 'http://webradio.antennevorarlberg.at/hits', 'https://i46.servimg.com/u/f46/19/40/01/67/c17515.png'],
            ['ANTENNE VORARLBERG Love Songs', 'http://webradio.antennevorarlberg.at/lovesongs', 'https://i46.servimg.com/u/f46/19/40/01/67/c17516.png'],
            ['ANTENNE VORARLBERG Partymix', 'http://webradio.antennevorarlberg.at/partymix', 'https://i46.servimg.com/u/f46/19/40/01/67/c17517.png'],
            ['ANTENNE VORARLBERG Rock Radio', 'http://webradio.antennevorarlberg.at/rock', 'https://i46.servimg.com/u/f46/19/40/01/67/c17527.png'],   
            ['Arabella Austropop', 'http://arabella.stream.kapper.net:8005/arabellaaustropop', 'https://i46.servimg.com/u/f46/19/40/01/67/c17526.png'],
            ['Arabella Oberösterreich', 'http://arabella.stream.kapper.net:8002/arabellaooe', 'https://i46.servimg.com/u/f46/19/40/01/67/c17524.png'],
            ['Arabella Lovesongs', 'http://arabella.stream.kapper.net:8009/arabellalove', 'https://i46.servimg.com/u/f46/19/40/01/67/c17523.png'],
            ['Arabella Relax', 'http://arabella.stream.kapper.net:8015/heroldrelax', 'https://i46.servimg.com/u/f46/19/40/01/67/c17521.png'],
            ['Arabella Ti Amo', 'http://arabella.stream.kapper.net:8007/arabellatiamo', 'https://i46.servimg.com/u/f46/19/40/01/67/c17525.png'],        
            ['KroneHit 105.8 FM', 'http://onair-ha1.krone.at/kronehit-hp.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok15.jpg'],
            ['Kronehit 90’s Dance', 'http://onair-ha1.krone.at/kronehit-90sdance.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok16.jpg'],
            ['Kronehit Beach Club', 'http://onair-ha1.krone.at/kronehit-event3.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok18.jpg'],
            ['Kronehit Black', 'http://onair-ha1.krone.at/kronehit-black.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok19.jpg'],
            ['KroneHit Best of 2017', 'http://onair.krone.at/kronehit-event3.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c17510.png'],
            ['Kronehit Clubland xxl', 'http://onair-ha1.krone.at/kronehit-clubland.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175132.png'],
            ['Kronehit Charts', 'http://onair.krone.at/kronehit-charts.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok22.jpg'],
            ['Kronehit Dance', 'http://onair-ha1.krone.at/kronehit-dance.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175131.png'],
            ['Kronehit Love', 'http://onair-ha1.krone.at/kronehit-love.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/c17510.png'],
            ['Life Radio', 'https://stream.liferadio.at/liferadio/mp3-192/radioat', 'https://i46.servimg.com/u/f46/19/40/01/67/lifera10.jpg'],
            ['Life Radio 80er', 'https://stream.liferadio.at/80er/mp3-192/radioat', 'https://i46.servimg.com/u/f46/19/40/01/67/lifera11.jpg'],
            ['Life Radio 90er', 'https://stream.liferadio.at/90er/mp3-192/radioat', 'https://i46.servimg.com/u/f46/19/40/01/67/lifera12.jpg'],
            ['VIENNA.AT - Lounge', 'http://webradio.vienna.at/vie-lounge', 'https://i46.servimg.com/u/f46/19/40/01/67/c17520.png']
            ]

<<<<<<< Updated upstream
        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?au_' + str(i), listitem=listItem, isFolder=True)
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
                    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?au_' + str(i),
                                                listitem=listitem, isFolder=True)
                    i = i + 1
                xbmcplugin.endOfDirectory(int(sys.argv[1]))

            else:

                Title = data['stanice'][int(self.opt2)]['nazov']
                Icon = data['stanice'][int(self.opt2)]['img']
                URL = data['stanice'][int(self.opt2)]['url']

                import radioPlayer as player
                player.Main().start(Title, Icon, URL)

        url = apiUrl.apiUrl + 'getAU'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            data = values
            test(self, selfGet)
        except requests.exceptions.RequestException as e:
            dialog = xbmcgui.Dialog()
            ok = dialog.ok(__addonname__, __addon__.getLocalizedString(30022))
>>>>>>> Stashed changes
