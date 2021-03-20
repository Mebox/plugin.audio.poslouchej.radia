# -*- coding: utf-8 -*-

import xbmc
import xbmcgui
import xbmcaddon
import os
import sys

__addon__ = xbmcaddon.Addon()
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

    def start(self, Title, Icon, URL):
        xbmc.executebuiltin('xbmc.activatewindow(1000)')
        xbmc.Player().stop()
        playList = xbmc.PlayList(xbmc.PLAYLIST_MUSIC)
        playList.clear()
        listItem = xbmcgui.ListItem(Title)
        listItem.setInfo('Music', infoLabels={'Title': Title})
        listItem.setArt({'icon': Icon})
        listItem.setArt({'thumb': Icon})
        listItem.setArt({'fanart': __addonpath__ + '//'+ 'fanart.jpg'})
        playList.add(URL, listItem)
        xbmc.Player().play(playList)
