#!/usr/bin/env python
"""
 *  Copyright (C) 2021 Mario Babinec (mr.babinec@gmail.com)
 *  This file is part of plugin.audio.poslouchej.radia
 *
 *  SPDX-License-Identifier: GPL-2.0-only
 *  See LICENSE.txt for more information.
"""

import json
import requests


class RadioApi:
    API_URL = 'https://moj-dennik.eu/api/'

    # get stations from api

    def get_sk_stations(self):
        url = self.API_URL + 'getSK'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_cz_stations(self):
        url = self.API_URL + 'getCZ'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_topsk_stations(self):
        url = self.API_URL + 'getTopSK'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_topcz_stations(self):
        url = self.API_URL + 'getTopCZ'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_newest_stations(self):
        url = self.API_URL + 'getNew'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_gb_stations(self):
        url = self.API_URL + 'getGB'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_usa_stations(self):
        url = self.API_URL + 'getUS'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_fra_stations(self):
        url = self.API_URL + 'getFR'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_ned_stations(self):
        url = self.API_URL + 'getNED'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_ger_stations(self):
        url = self.API_URL + 'getGER'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_pol_stations(self):
        url = self.API_URL + 'getPOL'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_au_stations(self):
        url = self.API_URL + 'getAU'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_rus_stations(self):
        url = self.API_URL + 'getRU'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    # get genres from api

    def get_dance_stations(self):
        url = self.API_URL + 'getDance'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_folk_stations(self):
        url = self.API_URL + 'getFolk'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_jazz_stations(self):
        url = self.API_URL + 'getJazz'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_word_stations(self):
        url = self.API_URL + 'getSlovo'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_oldies_stations(self):
        url = self.API_URL + 'getOldies'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_pop_stations(self):
        url = self.API_URL + 'getPop'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_relax_stations(self):
        url = self.API_URL + 'getRelax'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_rnb_stations(self):
        url = self.API_URL + 'getRnb'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_rock_stations(self):
        url = self.API_URL + 'getRock'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_solo_stations(self):
        url = self.API_URL + 'getSolo'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_news_stations(self):
        url = self.API_URL + 'getSpravodajske'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass


