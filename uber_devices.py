#!/usr/bin/env python3
import sys
import json
import requests
from config import CONFIG
import ubersmith

#pulls creds from ~/.uber.ini
USERNAME = CONFIG.get('UBER', 'uber_cuser')
API_TOKEN = CONFIG.get('UBER','uber_ctoken')

#for initial login
HEADERS = {
        'content-type': 'application/x-www-form-urlencoded',
        'accept': 'application/json'
        }

#paremters for access_token gen
def setUp(self):
    self.client - UbersmithClient(cfg['url'],
            cfg['username'],
            cfg['api_token'])

