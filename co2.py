#!/usr/bin/python3

import os
import configparser
import json
import requests
from datetime import datetime
from dateutil import tz
import mh_z19

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

date = datetime.now(tz.tzlocal()).isoformat()
co2 = int(mh_z19.read()['co2'])

url = config['co2']['api_url']
data = { 'fields': [date, co2] }
headers = { 'Content-Type': 'application/json' }

requests.post(url, data=json.dumps(data), headers=headers)
