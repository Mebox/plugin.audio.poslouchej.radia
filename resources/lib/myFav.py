# -*- coding: utf-8 -*-

import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import os
import sys
import json


__addon__ = xbmcaddon.Addon()
__addon_id__ = __addon__.getAddonInfo('id')
__addonname__ = __addon__.getAddonInfo('name')
__icon__ = __addon__.getAddonInfo('icon')
__addonpath__ = xbmc.translatePath(__addon__.getAddonInfo('path'))
__addondir__ = xbmc.translatePath(__addon__.getAddonInfo('profile'))
__lang__ = __addon__.getLocalizedString
__path__ = os.path.join(__addonpath__, 'resources', 'lib')
__path_img__ = os.path.join(__addonpath__, 'resources', 'media')

__userDataFolder__ = xbmc.translatePath("special://profile/addon_data/")

sys.path.append(__path__)
sys.path.append(__path_img__)


class Main:

    def start(self, selfGet):
        if not os.path.exists(__userDataFolder__ + 'myFav.json'):
            open(__userDataFolder__+ 'myFav.json', 'w').write('{"stanice": []}')
        with open(__userDataFolder__+ 'myFav.json', 'r') as file:
            data = json.load(file)

        # vars
        self = selfGet

        def test(self, selfGet):
            listitem = xbmcgui.ListItem()
            listitem.setArt({'fanart': __addonpath__ + '//' + 'fanart.jpg'})
            listitem.setProperty("IsPlaylist", "true")
            if self.opt2 == '':
                i = 0

                for element in data['stanice']:
                    listitem.setLabel(element['nazov'])
                    listitem.setArt({'clearLogo': element['url']})
                    listitem.setArt({'icon': element['img']})
                    listitem.setArt({'poster': element['img']})  # pre kodi < MATRIX
                    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?mf_' + str(i),
                                                listitem=listitem, isFolder=True)
                    i = i + 1
                xbmcplugin.endOfDirectory(int(sys.argv[1]))

            else:

                Title = data['stanice'][int(self.opt2)]['nazov']
                Icon = data['stanice'][int(self.opt2)]['img']
                URL = data['stanice'][int(self.opt2)]['url']

                import radioPlayer as player
                player.Main().start(Title, Icon, URL)

        test(self, selfGet)
