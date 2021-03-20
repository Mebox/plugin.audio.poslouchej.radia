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
                        ['Impuls Rádio', 'http://icecast5.play.cz/impuls128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioi12.jpg'],
			['Český rozhlas 1 - Rádiožurnál', 'http://icecast8.play.cz/cro1-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radior12.jpg'],
			['Evropa 2', 'http://ice.actve.net/fm-evropa2-128', 'https://i62.servimg.com/u/f62/19/40/01/67/radioe11.jpg'],
			['Frekvence 1', 'http://ice.actve.net/fm-frekvence1-128', 'https://i62.servimg.com/u/f62/19/40/01/67/radiof16.jpg'],
			['Rádio Blaník', 'http://ice.abradio.cz/blanikfm128.mp3?i=86.22812972256186', 'https://i62.servimg.com/u/f62/19/40/01/67/radiob12.jpg'],
			['Hitrádio FM', 'http://ice.abradio.cz/hitradiofm128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/hitrad15.jpg'],
			['Rádio Kiss', 'http://icecast4.play.cz:8000/kiss128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiok13.jpg'],
			['Český rozhlas 2 - Praha', 'http://icecast6.play.cz/cro2-128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc22.jpg'],
			['Rádio Beat', 'http://icecast2.play.cz/radiobeat128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/beat10.png'],
			['Country Rádio', 'http://icecast4.play.cz/country128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc33.jpg'],
            ]

        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?topCZ_' + str(i), listitem=listItem, isFolder=True)
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
                    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?topCZ_' + str(i),
                                                listitem=listitem, isFolder=True)
                    i = i + 1
                xbmcplugin.endOfDirectory(int(sys.argv[1]))

            else:

                Title = data['stanice'][int(self.opt2)]['nazov']
                Icon = data['stanice'][int(self.opt2)]['img']
                URL = data['stanice'][int(self.opt2)]['url']

                import radioPlayer as player
                player.Main().start(Title, Icon, URL)

        url = apiUrl.apiUrl + 'getTopCZ'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            data = values
            test(self, selfGet)
        except requests.exceptions.RequestException as e:
            dialog = xbmcgui.Dialog()
            ok = dialog.ok(__addonname__, __addon__.getLocalizedString(30022))
>>>>>>> Stashed changes
