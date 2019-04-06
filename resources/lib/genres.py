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
		['Dance/Electronica', sys.argv[0] + '?da', 'dance.png', '', getSettingBool('styl_dance')],
		['Folk/Country', sys.argv[0] + '?fo', 'folk.png', '', getSettingBool('styl_folk')],
		['Jazz/Blues/Soul', sys.argv[0] + '?ja', 'jazz.png', '', getSettingBool('styl_jazz')],
		[ADDON.getLocalizedString(30012), sys.argv[0] + '?ms', 'slovo.png', '', getSettingBool('styl_mluvene_slovo')],
		['Oldies', sys.argv[0] + '?ol', 'oldies.png', '', getSettingBool('styl_oldies')],
		['Pop', sys.argv[0] + '?po', 'pop.png', '', getSettingBool('styl_pop')],
		[ADDON.getLocalizedString(30013), sys.argv[0] + '?re', 'relax.png', '', getSettingBool('styl_relax')],
		['RnB/Hip Hop/Reggae', sys.argv[0] + '?rbn', 'rnb.png', '', getSettingBool('styl_rbn')],
		['Rock/Metal', sys.argv[0] + '?ro', 'rock.png', '', getSettingBool('styl_rock')],
		[ADDON.getLocalizedString(30014), sys.argv[0] + '?sp', 'solo.png', '', getSettingBool('styl_solopro')],
		[ADDON.getLocalizedString(30015), sys.argv[0] + '?zp', 'zpravodajsky.png', '', getSettingBool('stylzpravodajsky')],
               ]

	for v in list:
	    if not v[4]: continue
            listItem = xbmcgui.ListItem(label=v[0], iconImage=__path_img__ + '//' + v[2])
            xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=v[1], listitem=listItem, isFolder=True)
        
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


        
            
