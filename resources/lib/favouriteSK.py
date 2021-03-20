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
            ['Rádio Expres', 'http://stream.expres.sk:8000/96.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radioe15.jpg'],
			['Rádio Slovensko', 'http://icecast.stv.livebox.sk/slovensko_128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radios12.jpg'],
			['Fun Rádio', 'http://stream.funradio.sk:8000/fun128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiof20.jpg'],
			['Rádio Vlna', 'http://stream.radiovlna.sk/vlna-hi.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiov11.jpg'],
			['Europa 2', 'http://stream.radioservices.sk/europa2.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radioe11.jpg'],
			['Rádio Regina Západ', 'http://icecast.stv.livebox.sk/regina-ba_128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior10.jpg'],
			['Rádio Jemné', 'http://stream.jemne.sk/jemne-hi.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radioj11.jpg'],
			['Rádio Anténa Rock', 'http://stream.antenarock.sk/antena-hi.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior16.jpg'],
			['Rádio FM', 'http://icecast.stv.livebox.sk/fm_128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiof18.jpg'],
			['Rádio Lumen', 'http://audio.lumen.sk:8000/live128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiol10.jpg'],
            ]

        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?topSK_' + str(i), listitem=listItem, isFolder=True)
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
                    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?topSK_' + str(i),
                                                listitem=listitem, isFolder=True)
                    i = i + 1
                xbmcplugin.endOfDirectory(int(sys.argv[1]))

            else:

                Title = data['stanice'][int(self.opt2)]['nazov']
                Icon = data['stanice'][int(self.opt2)]['img']
                URL = data['stanice'][int(self.opt2)]['url']

                import radioPlayer as player
                player.Main().start(Title, Icon, URL)

        url = apiUrl.apiUrl + 'getTopSK'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            data = values
            test(self, selfGet)
        except requests.exceptions.RequestException as e:
            dialog = xbmcgui.Dialog()
            ok = dialog.ok(__addonname__, __addon__.getLocalizedString(30022))
>>>>>>> Stashed changes
