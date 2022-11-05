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
    API_URL = 'https://radia.moj-dennik.eu/api/get-stations'

    # get stations from api

    def get_sk_stations(self):
        url = self.API_URL + '?country=sk'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_cz_stations(self):
        url = self.API_URL + '?country=cz'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_topsk_stations(self):
        url = self.API_URL + '?country=sk&top=1'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_topcz_stations(self):
        url = self.API_URL + '?country=cz&top=1'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_newest_stations(self):
        url = self.API_URL + '?recent=1'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_gb_stations(self):
        url = self.API_URL + '?country=uk'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_usa_stations(self):
        url = self.API_URL + '?country=us'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_fra_stations(self):
        url = self.API_URL + '?country=fr'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_ned_stations(self):
        url = self.API_URL + '?country=ned'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_ger_stations(self):
        url = self.API_URL + '?country=ger'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_pol_stations(self):
        url = self.API_URL + '?country=pol'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_au_stations(self):
        url = self.API_URL + '?country=au'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_rus_stations(self):
        url = self.API_URL + '?country=ru'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_slo_stations(self):
            url = self.API_URL + '?country=slo'
            try:
                response = requests.get(url)
                values = json.loads(response.content.decode('utf-8'))
                return values
            except requests.exceptions.RequestException as e:
                pass

    # get genres from api

    def get_dance_stations(self):
        url = self.API_URL + '?style=dance'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_folk_stations(self):
        url = self.API_URL + '?style=folk'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_jazz_stations(self):
        url = self.API_URL + '?style=jazz'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_word_stations(self):
        url = self.API_URL + '?style=talk'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_oldies_stations(self):
        url = self.API_URL + '?style=oldies'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_pop_stations(self):
        url = self.API_URL + '?style=pop'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_relax_stations(self):
        url = self.API_URL + '?style=relax'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_rnb_stations(self):
        url = self.API_URL + '?style=rnb'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_rock_stations(self):
        url = self.API_URL + '?style=rock'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_solo_stations(self):
        url = self.API_URL + '?style=solo'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass

    def get_news_stations(self):
        url = self.API_URL + '?style=news'
        try:
            response = requests.get(url)
            values = json.loads(response.content.decode('utf-8'))
            return values
        except requests.exceptions.RequestException as e:
            pass


