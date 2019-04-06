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

ADDON = xbmcaddon.Addon(id='plugin.radio.cz_sk_word')

sys.path.append(__path__)
sys.path.append (__path_img__)

class Main:

    def start(self, selfGet):
    	
	def getSettingBool(setting):
            return __addon__.getSetting(setting).strip().decode('utf-8').lower() == "true"

        # vars
        self = selfGet
    
        list = [
		[ADDON.getLocalizedString(30002), sys.argv[0] + '?sk', 'radioSlovakia.png', '', getSettingBool('radio_Slovakia')],
        	[ADDON.getLocalizedString(30003), sys.argv[0] + '?cz', 'radioCzechRepublic.png', '', getSettingBool('radio_Czech_Republic')],
		[ADDON.getLocalizedString(30004), sys.argv[0] + '?uk', 'radioUnitedKingdom.png', '', getSettingBool('radio_United_Kingdom')],
		[ADDON.getLocalizedString(30005), sys.argv[0] + '?us', 'radioUnitedStates.png', '', getSettingBool('radio_United_States')],
		[ADDON.getLocalizedString(30006), sys.argv[0] + '?fr', 'radioFrance.png', '', getSettingBool('radio_France')],
		[ADDON.getLocalizedString(30007), sys.argv[0] + '?nl', 'radioNetherlands.png', '', getSettingBool('radio_Netherland')],
		[ADDON.getLocalizedString(30008), sys.argv[0] + '?ger', 'radioGermany.png', '', getSettingBool('radio_Germany')],
        	[ADDON.getLocalizedString(30009), sys.argv[0] + '?pl', 'radioPolskie.png', '', getSettingBool('radio_Polskie')],
		[ADDON.getLocalizedString(30010), sys.argv[0] + '?au', 'radioAustria.png', '', getSettingBool('radio_Austria')],
        	[ADDON.getLocalizedString(30011), sys.argv[0] + '?ru', 'radioRussianFederation.png', '', getSettingBool('radio_Russian_Federation')],
            ]

	for v in list:
	    if not v[4]: continue
            listItem = xbmcgui.ListItem(label=v[0], iconImage=__path_img__ + '//' + v[2])
            xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=v[1], listitem=listItem, isFolder=True)
        
        xbmcplugin.endOfDirectory(int(sys.argv[1]))