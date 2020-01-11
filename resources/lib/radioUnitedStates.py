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
            ['181.fm Super 70s', 'http://relay.181.fm:8066', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm Awesome 80s', 'http://mp3uplink.duplexfx.com:8000', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm Lite 80s', 'http://relay.181.fm:8040?.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm 80s Hairband', 'http://mp3uplink.duplexfx.com:8014', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm 90s Alternative', 'http://uplink.duplexfx.com:8052', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm 90s Country', 'http://uplink.duplexfx.com:8050', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm Star 90s', 'http://relay3.181.fm:8012', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm Beatles', 'http://relay.181.fm:8062', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm Classic Hits', 'http://listen.181fm.com/181-greatoldies_128k.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm Classical Guitar', 'http://mp3uplink.duplexfx.com:8020', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm Good Time Oldies', 'http://mp3uplink.duplexfx.com:8046', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm Great Oldies', 'http://mp3uplink.duplexfx.com:8046', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm Highway 181', 'http://mp3uplink.duplexfx.com:8018', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm Jammin 181', 'http://mp3uplink.duplexfx.com:8042', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm Old School', 'http://relay.181.fm:8068', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm Party 181', 'http://uplink.duplexfx.com:8036', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm POWER 181', 'http://relay.181.fm:8128', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm Reggae Roots', 'http://relay2.181.fm:8096', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm Real Country', 'http://relay.181.fm:8034', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm Soul', 'http://181fm-edge1.cdnstream.com/181-soul_128k.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm The Breeze', 'http://relay.181.fm:8004', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm The Buzz', 'http://relay.181.fm:8126', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm The Eagle', 'http://uplink.duplexfx.com:8030', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm The Heart', 'http://uplink.duplexfx.com:8006', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm The Mix Channel', 'http://relay.181.fm:8032', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm The Office', 'http://relay.181.fm:8002', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm The Beat', 'http://uplink.duplexfx.com:8054', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm The Box', 'http://relay2.181.fm:8024/?type=.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm True RNB', 'http://mp3uplink.duplexfx.com:8022', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm Rock 40', 'http://mp3uplink.duplexfx.com:8028', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm Rock 181', 'http://uplink.duplexfx.com:8008', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm The Rock!', 'http://relay5.181.fm:8064', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['113 FM Awesome 80s', 'http://113fm-edge1.cdnstream.com/1762_128', 'https://i11.servimg.com/u/f11/19/40/01/67/113fm10.png'],
            ['BeGoodRadio 80s Jazz', 'http://75.126.5.154/5210_128', 'https://i11.servimg.com/u/f11/19/40/01/67/d4b66910.png'],
            ['BeGoodRadio 80s Lite', 'http://75.126.5.154/5211_128', 'https://i11.servimg.com/u/f11/19/40/01/67/d4b66910.png'],
            ['BeGoodRadio 80s Metal', 'http://75.126.5.154/5212_128', 'https://i11.servimg.com/u/f11/19/40/01/67/d4b66910.png'],
            ['BeGoodRadio 80s Mix', 'http://75.126.5.154/5213_128', 'https://i11.servimg.com/u/f11/19/40/01/67/d4b66910.png'],
            ['BeGoodRadio 80s New Wave', 'http://75.126.5.154/5214_128', 'https://i11.servimg.com/u/f11/19/40/01/67/d4b66910.png'],
            ['BeGoodRadio 80s Office', 'http://75.126.5.154/5215_128', 'https://i11.servimg.com/u/f11/19/40/01/67/d4b66910.png'],
            ['BeGoodRadio 80s Pop', 'http://75.126.5.154/5216_128', 'https://i11.servimg.com/u/f11/19/40/01/67/d4b66910.png'],
            ['BeGoodRadio 80s Pop Rock', 'http://75.126.5.154/5217_128', 'https://i11.servimg.com/u/f11/19/40/01/67/d4b66910.png'],
            ['BeGoodRadio 80s Punk Rock', 'http://75.126.5.154/5218_128', 'https://i11.servimg.com/u/f11/19/40/01/67/d4b66910.png'],
            ['BeGoodRadio 80s Rock Mix', 'http://75.126.5.154/5219_128', 'https://i11.servimg.com/u/f11/19/40/01/67/d4b66910.png'],
            ['Best Net Radio 70s and 80s', 'http://bigrradio.cdnstream1.com/5141_128', 'https://i46.servimg.com/u/f46/19/40/01/67/c175128.png'],
            ['Best Net Radio 80s and 90s Mix', 'http://bigrradio.cdnstream1.com/5143_128', 'https://i46.servimg.com/u/f46/19/40/01/67/c175128.png'],
            ['Best Net Radio 80s Mellow', 'http://bigrradio.cdnstream1.com/5145_128', 'https://i46.servimg.com/u/f46/19/40/01/67/c175128.png'],
            ['Best Net Radio Country Oldies', 'http://bigrradio.cdnstream1.com/5158_128', 'https://i46.servimg.com/u/f46/19/40/01/67/c175128.png'],
            ['Best Net Radio Coffee House', 'http://bigrradio.cdnstream1.com/5156_128', 'https://i46.servimg.com/u/f46/19/40/01/67/c175128.png'],
            ['Best Net Radio Love Channel', 'http://bigrradio.cdnstream1.com/5161_128', 'https://i46.servimg.com/u/f46/19/40/01/67/c175128.png'],
            ['Best Net Radio New Wave', 'http://bigrradio.cdnstream1.com/5161_128', 'https://i46.servimg.com/u/f46/19/40/01/67/c175128.png'],
            ['Epic Rock Radio', 'http://listen.sonixfm.com:8734/stream', 'https://i11.servimg.com/u/f11/19/40/01/67/err-lo10.jpg'],
            ['Powerhitz', 'http://powerhitz.powerhitz.com:2228?.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop15.jpg'],
            ['Powerhitz - Classic Rock', 'http://jbmedia-edge1.cdnstream.com/pureclassicrock?listenerid=d7c0601fef8d4074a4f69e8fb6a214fa&cb=211272.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop15.jpg'],
            ['Powerhitz - 90s Area', 'http://jbmedia-edge1.cdnstream.com/90sarea?listenerid=d7c0601fef8d4074a4f69e8fb6a214fa&cb=717408.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop15.jpg'],
            ['Powerhitz - The Hitlist', 'http://jbmedia-edge1.cdnstream.com/hitlist?cb=718368.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop15.jpg'],
            ['Powerhitz - Ultimate 80s', 'http://jbmedia-edge1.cdnstream.com/ultimate80s?listenerid=d7c0601fef8d4074a4f69e8fb6a214fa&cb=712079.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop15.jpg'],
            ['Radio Danz', 'http://107.182.230.133/stream?icy=http', 'https://i62.servimg.com/u/f62/19/40/01/67/radio_13.png'],
            ['RADIO TROP ROCK', 'http://usa14.fastcast4u.com:5224/stream/1/', 'https://i46.servimg.com/u/f46/19/40/01/67/c175129.png'],
            ['Third Rock Radio', 'http://rfcmedia2.streamguys1.com/thirdrock.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175126.png']
            ]

        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?us_' + str(i), listitem=listItem, isFolder=True)
                i = i + 1
            xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
        else:
        
            Title = list[int(self.opt2)][0]
            Icon = list[int(self.opt2)][2]
            URL = list[int(self.opt2)][1]
        
            import radioPlayer as player
            player.Main().start(Title, Icon, URL)
            
