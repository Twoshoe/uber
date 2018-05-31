#!/usr/bin/env python3
import sys
import json
import requests
import ubersmith
import base64
import urllib
import urllib2
from config import CONFIG

#pulls creds from ~/.uber.ini
USERNAME = CONFIG.get('UBER', 'UBER_CUSER')
API_TOKEN = CONFIG.get('UBER','UBER_CTOKEN')

#for initial login
HEADERS = {
        'content-type': 'application/x-www-form-urlencoded',
        'accept': 'application/json'
        }

#paremters for access_token gen
def setUp(self):
    self.client - UbersmithClient(cfg['URL'],
            cfg['USERNAME'],
            cfg['API_TOKEN'])

