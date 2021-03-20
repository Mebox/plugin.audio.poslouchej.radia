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
            ['Blues Sky (CZ)', 'https://node-05.zeno.fm/0hx4b9zscseuv?rj-ttl=5&rj-tok=AAABcQzR__wA_g1Ji3kf17PHog', 'https://i46.servimg.com/u/f46/19/40/01/67/blues_10.jpg'],
            ['Český Rozhlas Jazz (CZ)', 'http://icecast2.play.cz:8000/crojazz128aac', 'https://i62.servimg.com/u/f62/19/40/01/67/radioj14.jpg'],
            ['E-Radio JAZZINEC (CZ)', 'http://ice3.abradio.cz/jazzinec128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioj10.jpg'],
            ['101 Smooth Jazz Mellow Mix (GB)', 'https://edge3.peta.live365.net/b48071_128mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175149.png'],
            ['Magic Soul (GB)', 'http://icy-e-bz-08-boh.sharp-stream.com/magicsoul.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175140.png'],
            ['Relaxing Jazz (GB)', 'http://stream-02-eu.relaxingjazz.com/stream/1/', 'https://i46.servimg.com/u/f46/19/40/01/67/c175150.png'],
            ['181.fm Soul (USA)', 'http://181fm-edge1.cdnstream.com/181-soul_128k.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['BeGoodRadio 80s Jazz (USA)', 'http://75.126.5.154/5210_128', 'https://i11.servimg.com/u/f11/19/40/01/67/d4b66910.png']
            ]

        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?ja_' + str(i), listitem=listItem, isFolder=True)
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
                    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?ja_' + str(i),
                                                listitem=listitem, isFolder=True)
                    i = i + 1
                xbmcplugin.endOfDirectory(int(sys.argv[1]))

            else:

                Title = data['stanice'][int(self.opt2)]['nazov']
                Icon = data['stanice'][int(self.opt2)]['img']
                URL = data['stanice'][int(self.opt2)]['url']

                import radioPlayer as player
                player.Main().start(Title, Icon, URL)

        url = apiUrl.apiUrl + 'getJazz'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            data = values
            test(self, selfGet)
        except requests.exceptions.RequestException as e:
            dialog = xbmcgui.Dialog()
            ok = dialog.ok(__addonname__, __addon__.getLocalizedString(30022))
>>>>>>> Stashed changes
