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
            ['Rádio 7', 'http://play.twr.sk:8000/128', 'https://i11.servimg.com/u/f11/19/40/01/67/radio710.jpg'],
		        ['Rádio Aetter', 'http://stream.aetter.sk:8000/aetter', 'https://i46.servimg.com/u/f46/19/40/01/67/aetter10.jpg'],
                        ['Rádio Anténa Rock', 'http://stream.antenarock.sk/antena-hi.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior16.jpg'],
			['Rádio Anténa Rock Hard', 'http://stream.radioservices.sk/hardrock.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior17.jpg'],
			['Rádio Best FM', 'http://stream2.bestfm.sk:80/128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiob10.jpg'],
			['Rádio Beta', 'http://109.71.67.102:8000/beta_live_high.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiob11.jpg'],
			['Rádio Beta - České a Slovenské hity', 'http://109.71.67.102:8000/beta_cspop.mp3', 'https://i.servimg.com/u/f62/19/40/01/67/betacz10.jpg'],
			['Rádio Beta - Hity 80s a 90s', 'http://109.71.67.102:8000/beta_80a90.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/beta8010.jpg'],
			['Rádio Beta - Hráme Jubilantom', 'http://109.71.67.102:8000/beta_jubilanti.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/betaju10.jpg'],
			['Rádio Blesk', 'http://stream.radioblesk.net:7777/;stream/1', 'https://i11.servimg.com/u/f11/19/40/01/67/radiob12.jpg'],
			['Rádio Devín', 'http://icecast.stv.livebox.sk/devin_128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiod11.jpg'],
			['Dobré Rádio', 'http://stream.dobreradio.sk:8813/dobreradio.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/dobrer10.jpg'],
			['Europa2 SK', 'http://stream.radioservices.sk/europa2.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radioe11.jpg'],
			['Rádio Expres', 'http://stream.expres.sk:8000/96.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radioe15.jpg'],
		        ['Rádio Dychovka', 'https://listen.radioking.com/radio/307817/stream/354746', 'https://i.servimg.com/u/f46/19/40/01/67/dychov10.jpg'],
			['Rádio_FM', 'http://icecast.stv.livebox.sk/fm_128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiof18.jpg'],
			['Rádio Frontinus', 'http://stream.frontinus.sk:8000/frontinus128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiof19.jpg'],
			['Fun Rádio', 'http://stream.funradio.sk:8000/fun128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiof20.jpg'],
			['Fun Rádio 80. - 90. roky', 'http://stream.funradio.sk:8000/80-90-128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiof21.jpg'],
			['Fun Rádio CZ-SK', 'http://stream.funradio.sk:8000/cs128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiof22.jpg'],
			['Fun Rádio Dance', 'http://stream.funradio.sk:8000/dance128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiof23.jpg'],
        		['Fresh Radio', 'http://164.68.122.137:8002/;stream/1', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_40.jpg'],
			['G-Radio', 'http://88.212.34.18:8050/mp3midband', 'https://i11.servimg.com/u/f11/19/40/01/67/radiog10.jpg'],
                        ['Rádio Goldies', 'http://icecast.radiosity.sk:8000/oldies.mp3', 'https://i.servimg.com/u/f46/19/40/01/67/goldie10.jpg'],
			['Info Vojna', 'http://stream.infovojna.sk:8000/live128', 'https://i62.servimg.com/u/f62/19/40/01/67/radioi15.jpg'],
			['Rádio Janko Hraško', 'http://78.24.9.110:31088/;stream/1', 'https://i11.servimg.com/u/f11/19/40/01/67/radioj10.jpg'],
		        ['Rádio Jemné', 'http://stream.jemne.sk/jemne-hi.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radioj11.jpg'],
			['Rádio Jemné Chillout', 'http://stream.radioservices.sk/chillout.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radioj12.jpg'],
			['Rádio Junior', 'http://icecast.stv.livebox.sk/junior_128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radioj13.jpg'],
			['Rádio Jupiter', 'http://radio.treecom.net/jupiter_128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/radioj10.jpg'],
			['Rádio Kiks', 'http://ca6.rcast.net:4044/;stream/1', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_11.jpg'],
		        ['Rádio Kiss', 'http://radio.treecom.net/kissmp3_128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiok11.jpg'],
			['Rádio Košice', 'http://stream.ecce.sk:8000/radiokosice-128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiok12.jpg'],
			['Rádio Litera', 'http://icecast.stv.livebox.sk/litera_128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiol12.jpg'],
			['Rádio Lumen', 'http://audio.lumen.sk:8000/live128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiol10.jpg'],
                        ['Rádio Mária Slovensko', 'https://dreamsiteradiocp5.com/proxy/radiomariaslovensko?mp=/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/maria10.jpg'],
			['Rádio Modra', 'http://185.98.208.12:8000/;stream/1', 'https://i11.servimg.com/u/f11/19/40/01/67/radiom11.jpg'],
		        ['New Model Radio', 'http://stream.sepia.sk:8000/newmodel128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radion11.jpg'],
			['Nonstop Rádio', 'http://nonstop.out.airtime.pro:8000/nonstop_a', 'https://i11.servimg.com/u/f11/19/40/01/67/radion10.jpg'],
			['Rádio Patria', 'http://icecast.stv.livebox.sk/patria_128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiop13.jpg'],
			['Rádio Piešťany', 'http://live.radiopiestany.sk:8000/live.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiop12.jpg'],
			['Rádio Pohoda', 'http://mpc.mediacp.eu:8018/;stream/1', 'https://i46.servimg.com/u/f46/19/40/01/67/radiop10.jpg'],
			['Rádio Pyramída', 'http://icecast.stv.livebox.sk/pyramida_128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiop21.jpg'],
			['Rádio Rebeca', 'http://allnet.radionet.sk:8000/radiorebeca.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior14.jpg'],
			['Rádio Regina Západ', 'http://icecast.stv.livebox.sk/regina-ba_128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior10.jpg'],
			['Rádio Regina Stred', 'http://icecast.stv.livebox.sk/regina-bb_128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior10.jpg'],
			['Rádio Regina Východ', 'http://icecast.stv.livebox.sk/regina-ke_128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radior10.jpg'],
			['Rádio SiTy', 'http://icecast.radiosity.sk:8000/hq.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radios16.jpg'],
			['Rádio Slovakia International', 'http://icecast.stv.livebox.sk/rsi_128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radios15.jpg'],
			['Rádio Slovensko', 'http://icecast.stv.livebox.sk/slovensko_128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radios12.jpg'],
			['SKY Rádio', 'http://stream.skyradio.sk:8000/sky128', 'https://i11.servimg.com/u/f11/19/40/01/67/radios17.jpg'],
		        ['TLIS Rádio', 'https://stream.tlis.sk/tlis.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_21.jpg'],
		        ['Trnavské rádio', 'http://stream.trnavskeradio.sk/trnavske', 'https://i62.servimg.com/u/f62/19/40/01/67/radiot12.jpg'],
			['Rádio Viva Metropol', 'http://stream.sepia.sk:8000/viva128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiov12.jpg'],
			['Rádio Vlna', 'http://stream.radiovlna.sk/vlna-hi.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiov11.jpg'],
			['Rádio Vlna Golden Hits', 'http://stream.radioservices.sk/goldenhits.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiov10.jpg'],
                        ['Rádio X ', 'http://158.193.82.41:8000/radiox_128.mp3', 'https://i.servimg.com/u/f11/19/40/01/67/radiox15.jpg'],
			['Rádio X - Chillout X ', 'http://158.193.82.41:8000/chillout.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radioc10.jpg'],
			['Rádio X - DnB X ', 'http://158.193.82.41:8000/dnb.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiox12.jpg'],
			['Rádio X - Folklore X ', 'http://158.193.82.41:8000/ludovky.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/radio_13.jpg'],
			['Rádio X - Metal X ', 'http://158.193.82.41:8000/metal.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiox11.jpg'],
			['Rádio X - Oldies X ', 'http://158.193.82.41:8000/oldies.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiox10.jpg'],
			['Záhorácke Rádio', 'http://live.zahorackeradio.sk:8000/zr128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radioz10.jpg']
            ]

        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?sk_' + str(i), listitem=listItem, isFolder=True)
                i = i + 1
            xbmcplugin.endOfDirectory(int(sys.argv[1]))

        else:

            Title = list[int(self.opt2)][0]
            Icon = list[int(self.opt2)][2]
            URL = list[int(self.opt2)][1]

            import radioPlayer as player
            player.Main().start(Title, Icon, URL)
