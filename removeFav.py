# -*- coding: utf-8 -*-
"""
 *  Copyright (C) 2021 Mario Babinec (mr.babinec@gmail.com)
 *  This file is part of plugin.audio.poslouchej.radia
 *
 *  SPDX-License-Identifier: GPL-2.0-only
 *  See LICENSE.txt for more information.
"""

import sys
import xbmc
import xbmcvfs
import xbmcaddon
import xbmcgui
import json

__addon__ = xbmcaddon.Addon(id='plugin.audio.poslouchej.radia')
__addonname__ = __addon__.getAddonInfo('name')
__lang__ = __addon__.getLocalizedString
__userDataFolder__ = xbmcvfs.translatePath("special://profile/addon_data/plugin.audio.poslouchej.radia/")

if __name__ == '__main__':
    message = "Stanica: '{}'".format(sys.listitem.getLabel())
    xbmcgui.Dialog().notification("Úspešne dstránená!", message)

    with open(__userDataFolder__ + 'myFav.json') as data_file:
        old_data = json.load(data_file)
    dicts = old_data['stanice']

    for e in range(len(dicts) - 1, -1, -1):
        if dicts[e]['nazov'] == sys.listitem.getLabel():
            dicts.pop(e)
    old_data['stanice'] = dicts

    with open(__userDataFolder__ + 'myFav.json', 'w+') as outfile:
        json.dump(old_data, outfile)
    xbmc.executebuiltin("Container.Refresh()")
