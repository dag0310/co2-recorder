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

print(f"CO2: {co2} ppm")

url = config['co2']['api_url']
data = { 'fields': [date, co2] }
headers = { 'Content-Type': 'application/json' }

requests.post(url, data=json.dumps(data), headers=headers)
print(f"CO2 level sent to API {url}")

co2_filepath = config['co2']['co2_filepath']
with open(co2_filepath, 'w') as writer:
    writer.write(str(co2))
    print(f"CO2 level written to {co2_filepath}")
