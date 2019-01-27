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

class Main:

    def start(self, selfGet):
    
        # vars
        self = selfGet
    
        list = [
['Sky Radio 101 FM', 'https://playerservices.streamtheworld.com/api/livestream-redirect/SKYRADIO.mp3?dist=radionet', 'https://i46.servimg.com/u/f46/19/40/01/67/c17575.png'],
['Sky Radio 80s Hits', 'https://20133.live.streamtheworld.com/SRGSTR04.mp3?dist=radionet', 'https://i46.servimg.com/u/f46/19/40/01/67/c17592.png'],
['Sky Radio 90s Hits', 'https://playerservices.streamtheworld.com/api/livestream-redirect/SRGSTR05.mp3?dist=radionet', 'https://i46.servimg.com/u/f46/19/40/01/67/c17593.png'],
['Sky Radio 00s Hits', 'https://playerservices.streamtheworld.com/api/livestream-redirect/SRGSTR06.mp3?dist=radionet', 'https://i46.servimg.com/u/f46/19/40/01/67/c17594.png'],
['Sky Radio Hits', 'https://playerservices.streamtheworld.com/api/livestream-redirect/SRGSTR01.mp3?dist=radionet', 'https://i46.servimg.com/u/f46/19/40/01/67/c17595.png'],
['Sky Radio Running Hits Starter', 'https://playerservices.streamtheworld.com/api/livestream-redirect/SRGSTR21.mp3?dist=radionet', 'https://i46.servimg.com/u/f46/19/40/01/67/c17596.png'],
['Sky Radio Christmas', 'https://playerservices.streamtheworld.com/api/livestream-redirect/SRGSTR08.mp3?dist=radionet', 'https://i46.servimg.com/u/f46/19/40/01/67/c17597.png'],
['Sky Radio Smooth Hits', 'https://playerservices.streamtheworld.com/api/livestream-redirect/SRGSTR15.mp3?dist=radionet', 'https://i46.servimg.com/u/f46/19/40/01/67/c17575.png'],
['Sky Radio Feel Good Hits', 'https://playerservices.streamtheworld.com/api/livestream-redirect/SRGSTR20.mp3?dist=radionet', 'https://i46.servimg.com/u/f46/19/40/01/67/c17575.png'],
['Sky Radio 10s Hits', 'https://playerservices.streamtheworld.com/api/livestream-redirect/SRGSTR19.mp3?dist=radionet', 'https://i46.servimg.com/u/f46/19/40/01/67/c17575.png'],
['Sky Radio Running Hits Gevorderd', 'https://playerservices.streamtheworld.com/api/livestream-redirect/SRGSTR22.mp3?dist=radionet', 'https://i46.servimg.com/u/f46/19/40/01/67/c17575.png'],
['Sky Radio Running Hits Expert', 'https://playerservices.streamtheworld.com/api/livestream-redirect/SRGSTR23.mp3?dist=radionet', 'https://i46.servimg.com/u/f46/19/40/01/67/c17575.png'],
['Sky Radio Running Hits Stretch & Relax', 'https://playerservices.streamtheworld.com/api/livestream-redirect/SRGSTR24.mp3?dist=radionet', 'https://i46.servimg.com/u/f46/19/40/01/67/c17575.png'],
['Sky Radio Summerhits', 'https://playerservices.streamtheworld.com/api/livestream-redirect/SRGSTR02.mp3?dist=radionet', 'https://i46.servimg.com/u/f46/19/40/01/67/c17575.png'],
['Sky Radio Singer-Songwriter', 'https://playerservices.streamtheworld.com/api/livestream-redirect/SRGSTR16.mp3?dist=radionet', 'https://i46.servimg.com/u/f46/19/40/01/67/c17575.png'],
['Radio Veronica', 'https://playerservices.streamtheworld.com/api/livestream-redirect/VERONICA.mp3?dist=radionet', 'https://i46.servimg.com/u/f46/19/40/01/67/c17576.png'],
['Radio 10 Gold 60s 70s', 'https://playerservices.streamtheworld.com/api/livestream-redirect/TLPSTR18.mp3?dist=radionet', 'https://i46.servimg.com/u/f46/19/40/01/67/c17577.png'],
['SLAM!', 'http://20853.live.streamtheworld.com/SLAM_MP3_SC?', 'https://i46.servimg.com/u/f46/19/40/01/67/c17578.png'],
['Deep FM', 'http://stream.deep.radio/sd', 'https://i46.servimg.com/u/f46/19/40/01/67/c17579.png'],
['Radio Stad Den Haag 97.2 FM', 'http://94.228.133.3:80/;stream.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios19.jpg'],
['Radio 10 Top 4000', 'https://playerservices.streamtheworld.com/api/livestream-redirect/TLPSTR24.mp3?dist=radionet', 'https://i46.servimg.com/u/f46/19/40/01/67/c17582.png'],
['Fantasy Italo Radio', 'http://italo.live-streams.nl/live', 'https://i46.servimg.com/u/f46/19/40/01/67/c17581.png']
            ]

        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?nl_' + str(i), listitem=listItem, isFolder=True)
                i = i + 1
            xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
        else:
        
            Title = list[int(self.opt2)][0]
            Icon = list[int(self.opt2)][2]
            URL = list[int(self.opt2)][1]
        
            import radioPlayer as player
            player.Main().start(Title, Icon, URL)
            