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
            ['COLOR Music Radio (CZ)', 'http://icecast6.play.cz/color192.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc19.jpg'],
            ['Funkstar Radio (CZ)', 'https://funkstar.radioca.st/stream?ver=153586', 'https://i46.servimg.com/u/f46/19/40/01/67/funkst10.jpg'],
            ['HipHopVibes Rádio (CZ)', 'http://mp3stream4.abradio.cz/hiphopvibes128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioh14.jpg'],
            ['Rádio Spin 96,2 FM (CZ)', 'http://icecast4.play.cz/spin128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios14.jpg'],
            ['Radio City (BG)', 'http://79.98.108.172:8022/', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc36.jpg'],
            ['181.fm True RNB (USA)', 'http://mp3uplink.duplexfx.com:8022', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['M1.FM - Urban (D)', 'http://tuner.m1.fm/urban.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/urban-10.jpg']
            ]

        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?rbn_' + str(i), listitem=listItem, isFolder=True)
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
                    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?rbn_' + str(i),
                                                listitem=listitem, isFolder=True)
                    i = i + 1
                xbmcplugin.endOfDirectory(int(sys.argv[1]))

            else:

                Title = data['stanice'][int(self.opt2)]['nazov']
                Icon = data['stanice'][int(self.opt2)]['img']
                URL = data['stanice'][int(self.opt2)]['url']

                import radioPlayer as player
                player.Main().start(Title, Icon, URL)

        url = apiUrl.apiUrl + 'getRnb'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            data = values
            test(self, selfGet)
        except requests.exceptions.RequestException as e:
            dialog = xbmcgui.Dialog()
            ok = dialog.ok(__addonname__, __addon__.getLocalizedString(30022))
>>>>>>> Stashed changes
