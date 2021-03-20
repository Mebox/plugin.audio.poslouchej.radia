# -*- coding: utf-8 -*-

import sys
import xbmc
import xbmcaddon
import xbmcgui
import json

__addon__ = xbmcaddon.Addon()
__addon_id__ = __addon__.getAddonInfo('id')
__addonname__ = __addon__.getAddonInfo('name')
__icon__ = __addon__.getAddonInfo('icon')
__addonpath__ = xbmc.translatePath(__addon__.getAddonInfo('path'))
__addondir__ = xbmc.translatePath(__addon__.getAddonInfo('profile'))

__userDataFolder__ = xbmc.translatePath("special://profile/addon_data/")

if __name__ == '__main__':
    xbmc.log('good')
    message = "Stanica: '{}'".format(sys.listitem.getLabel())
    xbmcgui.Dialog().notification("Úspešne dstránená!", message)

    with open(__userDataFolder__ + 'myFav.json') as data_file:
        old_data = json.load(data_file)
    dicts = old_data['stanice']


    xbmc.log(sys.listitem.getLabel())

    for e in range(len(dicts) - 1, -1, -1):
        if dicts[e]['nazov'] == sys.listitem.getLabel().decode('utf-8'):
            dicts.pop(e)
    old_data['stanice'] = dicts

    with open(__userDataFolder__ + 'myFav.json', 'w+') as outfile:
        json.dump(old_data, outfile)
    xbmc.executebuiltin("Container.Refresh()")
