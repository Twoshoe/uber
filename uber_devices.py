#!/usr/bin/env python3
import sys
import json
import requests
from config import CONFIG

#pulls creds from ~/.uber.ini
username = CONFIG.get('uber', 'USERNAME')
api_token = CONFIG.get('uber','ctoken')

#for initial login
HEADERS = {
        'content-type': 'application/x-www-form-urlencoded',
        'accept': 'application/json'
        }

#paremters for access_token gen
PARAMETERS = {
        'username': USERNAME,
        'token': PASSWORD,
        }

#def main():
#    '''Logs into BMS by Kaseya and adds locations (stored as json) to an account'''
#    #post header + parameter to receive json data with bearer access_token
#    auth_response = requests.post(API_URL, headers=HEADERS, data=PARAMETERS)

#    #Read Device info from file
#    with open(FILE_NAME) as json_data:
#        device_manager = json.load(json_data)
#        print(json.dumps(device_manager, sort_keys=True, indent=4))
#        #header for posting device infomation
#        device_header = {
#                'accept': 'accept': 'application/json',
#                'content-type': 'application/json',
#                'authorization': 'Bearer {0}'.format(token)
#                }
#        device_response = requests.post(DEVICE_URL, json=device_manger,
#                headers=device_header)

#        print(device_responce)


