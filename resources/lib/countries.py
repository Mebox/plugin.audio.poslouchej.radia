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
    			[__addon__.getLocalizedString(30002), sys.argv[0] + '?sk', 'radioSlovakia.png', '', getSettingBool('radio_Slovakia')],
            	[__addon__.getLocalizedString(30003), sys.argv[0] + '?cz', 'radioCzechRepublic.png', '', getSettingBool('radio_Czech_Republic')],
    			[__addon__.getLocalizedString(30004), sys.argv[0] + '?uk', 'radioUnitedKingdom.png', '', getSettingBool('radio_United_Kingdom')],
    			[__addon__.getLocalizedString(30005), sys.argv[0] + '?us', 'radioUnitedStates.png', '', getSettingBool('radio_United_States')],
    			[__addon__.getLocalizedString(30006), sys.argv[0] + '?fr', 'radioFrance.png', '', getSettingBool('radio_France')],
    			[__addon__.getLocalizedString(30007), sys.argv[0] + '?nl', 'radioNetherlands.png', '', getSettingBool('radio_Netherland')],
    			[__addon__.getLocalizedString(30008), sys.argv[0] + '?ger', 'radioGermany.png', '', getSettingBool('radio_Germany')],
            	[__addon__.getLocalizedString(30009), sys.argv[0] + '?pl', 'radioPolskie.png', '', getSettingBool('radio_Polskie')],
    			[__addon__.getLocalizedString(30010), sys.argv[0] + '?au', 'radioAustria.png', '', getSettingBool('radio_Austria')],
            	[__addon__.getLocalizedString(30011), sys.argv[0] + '?ru', 'radioRussianFederation.png', '', getSettingBool('radio_Russian_Federation')],
               ]

	for v in list:
	    if not v[4]: continue
            listItem = xbmcgui.ListItem(label=v[0], iconImage=__path_img__ + '//' + v[2])
            xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=v[1], listitem=listItem, isFolder=True)

        xbmcplugin.endOfDirectory(int(sys.argv[1]))
