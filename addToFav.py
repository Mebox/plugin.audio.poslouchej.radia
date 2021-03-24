# coding=utf-8
"""
 *  Copyright (C) 2021 Mario Babinec (mr.babinec@gmail.com)
 *  This file is part of plugin.audio.poslouchej.radia
 *
 *  SPDX-License-Identifier: GPL-2.0-only
 *  See LICENSE.txt for more information.
"""
import sys
import xbmcvfs
import xbmcaddon
import xbmcgui
import os
import json

__addon__ = xbmcaddon.Addon(id='plugin.audio.poslouchej.radia')
__addonname__ = __addon__.getAddonInfo('name')
__lang__ = __addon__.getLocalizedString
__userDataFolder__ = xbmcvfs.translatePath("special://profile/addon_data/plugin.audio.poslouchej.radia/")


if __name__ == '__main__':
    if not os.path.exists(__userDataFolder__ + 'myFav.json'):
        open(__userDataFolder__ + 'myFav.json', 'w').write('{"stanice": []}')

    with open(__userDataFolder__ + 'myFav.json') as data_file:
        old_data = json.load(data_file)

    # control if station is in list -leia
    dicts = old_data['stanice']

    for e in range(len(dicts) - 1, -1, -1):
        if dicts[e]['img'] == sys.listitem.getArt('icon'):
            dicts.pop(e)
    old_data['stanice'] = dicts

    z = {"nazov": "" + sys.listitem.getLabel() + "", "url": "" + sys.listitem.getPath() + "",
         "img": "" + sys.listitem.getArt('icon') + "", "is_custom": "0"}

    old_data['stanice'].append(z)

    with open(__userDataFolder__ + 'myFav.json', 'w+') as outfile:
        json.dump(old_data, outfile)

    message = "Stanica: '{}'".format(sys.listitem.getLabel())
    xbmcgui.Dialog().notification("Pridané medzi obľúbené!", message)

