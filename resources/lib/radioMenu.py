# -*- coding: utf-8 -*-

import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import os
import sys
import re


__addon__ = xbmcaddon.Addon(id='plugin.audio.poslouchej.radia')
__addon_id__ = __addon__.getAddonInfo('id')
__addonname__ = __addon__.getAddonInfo('name')
__icon__ = __addon__.getAddonInfo('icon')
__addonpath__ = xbmc.translatePath(__addon__.getAddonInfo('path'))
__lang__ = __addon__.getLocalizedString
__path__ = os.path.join(__addonpath__, 'resources', 'lib')
__path_img__ = os.path.join(__addonpath__, 'resources', 'media')

sys.path.append(__path__)
sys.path.append(__path_img__)


class Main:

    def start(self, selfGet):

        def getSettingBool(setting):
            return __addon__.getSetting(setting).strip().lower() == 'true'

        # vars
        self = selfGet

        list = [
            [__addon__.getLocalizedString(30001), sys.argv[0] + '?cou', 'countries.png', '',
             getSettingBool('radio_countries')],
            [__addon__.getLocalizedString(30016), sys.argv[0] + '?gen', 'genres.png', '',
             getSettingBool('radio_genres')],
            [__addon__.getLocalizedString(30017), sys.argv[0] + '?fav', 'star.png', '', getSettingBool('radio_fav')],
            [__addon__.getLocalizedString(30018), sys.argv[0] + '?new', 'new_added.png', '',
             getSettingBool('new_added')],
        ]

        for v in list:
            if not v[4]: continue
            listItem = xbmcgui.ListItem()
            listItem.setArt({'fanart': __addonpath__ + '//' + 'fanart.jpg'})
            listItem.setArt({'icon': __path_img__ + '//' + v[2]})
            listItem.setLabel(v[0])
            # xbmc.log(__path_img__ + '/' + v[2])
            xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=v[1], listitem=listItem, isFolder=True)

        xbmcplugin.endOfDirectory(int(sys.argv[1]))

        if self.opt != '':
            Title = list[int(self.opt)][0]
            Icon = list[int(self.opt)][2]
            URL = list[int(self.opt)][3]

            import radioPlayer as player
            player.Main().start(Title, Icon, URL)
