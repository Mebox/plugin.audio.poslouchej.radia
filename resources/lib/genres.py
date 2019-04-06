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

__addon__           = xbmcaddon.Addon(id='plugin.audio.poslouchej.radia')
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

	def getSettingBool(setting):
            return __addon__.getSetting(setting).strip().decode('utf-8').lower() == "true"

        # vars
        self = selfGet
    
        list = [
    			['Dance/Electronica', sys.argv[0] + '?da', 'genres.png', '', getSettingBool('styl_dance')],
    			['Folk/Country', sys.argv[0] + '?fo', 'genres.png', '', getSettingBool('styl_folk')],
    			['Jazz/Blues/Soul', sys.argv[0] + '?ja', 'genres.png', '', getSettingBool('styl_jazz')],
    			[__addon__.getLocalizedString(30012), sys.argv[0] + '?ms', 'genres.png', '', getSettingBool('styl_mluvene_slovo')],
    			['Oldies', sys.argv[0] + '?ol', 'genres.png', '', getSettingBool('styl_oldies')],
    			['Pop', sys.argv[0] + '?po', 'genres.png', '', getSettingBool('styl_pop')],
    			[__addon__.getLocalizedString(30013), sys.argv[0] + '?re', 'genres.png', '', getSettingBool('styl_relax')],
    			['RnB/Hip Hop/Reggae', sys.argv[0] + '?rbn', 'genres.png', '', getSettingBool('styl_rbn')],
    			['Rock/Metal', sys.argv[0] + '?ro', 'genres.png', '', getSettingBool('styl_rock')],
    			[__addon__.getLocalizedString(30014), sys.argv[0] + '?sp', 'genres.png', '', getSettingBool('styl_solopro')],
    			[__addon__.getLocalizedString(30015), sys.argv[0] + '?zp', 'genres.png', '', getSettingBool('stylzpravodajsky')],
               ]

	for v in list:
	    if not v[4]: continue
            listItem = xbmcgui.ListItem(label=v[0], iconImage=__path_img__ + '//' + v[2])
            xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=v[1], listitem=listItem, isFolder=True)

        xbmcplugin.endOfDirectory(int(sys.argv[1]))
