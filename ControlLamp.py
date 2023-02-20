import requests
from urllib3.exceptions import InsecureRequestWarning
import os
import time

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


DIRIGERA_IP = os.environ.get("DIRIGERA_IP")
DIRIGERA_TOKEN = os.environ.get("DIRIGERA_TOKEN")


devicesUrl = f"https://{DIRIGERA_IP}:8443/v1/devices"
headers = { "Authorization": f"Bearer {DIRIGERA_TOKEN}"}

device_id="ada4c059-1817-41ed-bff2-5d8432b4472c_1"
deviceUrl = f"{devicesUrl}/{device_id}"

deviceAttributes = [{ 
     "attributes": { "isOn": True }
    }]
response = requests.patch(deviceUrl, headers=headers, json=deviceAttributes, verify=False)

time.sleep(2)

deviceAttributes = [{ 
     "attributes": { "isOn": False }
    }]
response = requests.patch(deviceUrl, headers=headers, json=deviceAttributes, verify=False)
