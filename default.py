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

class Radio:
    def __init__(self):

        optMatches = re.compile('\?([^_]+)_?').findall(sys.argv[2])
        if len(optMatches) == 0:
            self.opt = ''
        else:
            self.opt = optMatches[0]

        optMatches2 = re.compile('_(.+)').findall(sys.argv[2])
        if len(optMatches2) == 0:
            self.opt2 = ''
        else:
            self.opt2 = optMatches2[0]



        if self.opt == 'cz':
            import radioCzechRepublic as start
        elif self.opt == 'sk':
            import radioSlovakia as start
        elif self.opt == 'topCZ':
            import favouriteCZ as start
        elif self.opt == 'topSK':
            import favouriteSK as start
        elif self.opt == 'fr':
            import radioFrance as start
        elif self.opt == 'nl':
            import radioNetherlands as start
        elif self.opt == 'ru':
            import radioRussianFederation as start
        elif self.opt == 'pl':
            import radioPolskie as start
        elif self.opt == 'us':
            import radioUnitedStates as start
        elif self.opt == 'uk':
            import radioUnitedKingdom as start
        elif self.opt == 'ger':
            import radioGermany as start
        elif self.opt == 'au':
            import radioAustria as start
        elif self.opt == 'fo':
            import stylfolk as start
        elif self.opt == 'da':
            import styldance as start
        elif self.opt == 'rbn':
            import stylrbn as start
        elif self.opt == 'ja':
            import styljazz as start
        elif self.opt == 'ol':
            import styloldies as start
        elif self.opt == 'po':
            import stylpop as start
        elif self.opt == 're':
            import stylrelax as start
        elif self.opt == 'ro':
            import stylrock as start
        elif self.opt == 'sp':
            import stylsolopro as start
        elif self.opt == 'ms':
            import stylmluveneslovo as start
        elif self.opt == 'zp':
            import stylzpravodajsky as start
        elif self.opt == 'cou':
            import countries as start
        elif self.opt == 'fav':
            import favourites as start
        elif self.opt == 'gen':
            import genres as start
        else:
            import radioMenu as start

        start.Main().start(self)

Radio()
