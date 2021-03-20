# coding=utf-8

import sys
import xbmc
import xbmcaddon
import xbmcgui
import os
import json

__addon__ = xbmcaddon.Addon()
__addon_id__ = __addon__.getAddonInfo('id')
__addonname__ = __addon__.getAddonInfo('name')
__icon__ = __addon__.getAddonInfo('icon')
__addonpath__ = xbmc.translatePath(__addon__.getAddonInfo('path'))
__addondir__ = xbmc.translatePath(__addon__.getAddonInfo('profile'))

__userDataFolder__ = xbmc.translatePath("special://profile/addon_data/")

if __name__ == '__main__':
    if not os.path.exists(__userDataFolder__ + 'myFav.json'):
        open(__userDataFolder__ + 'myFav.json', 'w').write('{"stanice": []}')

    with open(__userDataFolder__ + 'myFav.json') as data_file:
        old_data = json.load(data_file)

    z = {"nazov": "" + sys.listitem.getLabel() + "", "url": "" + sys.listitem.getArt('clearlogo') + "",
         "img": "" + sys.listitem.getArt('poster') + ""}

    added = old_data['stanice'].append(z)

    with open(__userDataFolder__ + 'myFav.json', 'w+') as outfile:
        json.dump(old_data, outfile)

    xbmc.log('good')
    message = "Stanica: '{}'".format(sys.listitem.getLabel())
    xbmcgui.Dialog().notification("Pridané medzi obľúbené!", message)
