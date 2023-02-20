import requests
import json
from urllib3.exceptions import InsecureRequestWarning
import os

DIRIGERA_IP = os.environ.get("DIRIGERA_IP")
DIRIGERA_TOKEN = os.environ.get("DIRIGERA_TOKEN")


requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
devices_url = f"https://{DIRIGERA_IP}:8443/v1/devices"
headers = { "Authorization": f"Bearer {DIRIGERA_TOKEN}"}

response = requests.get(devices_url, headers=headers, verify=False);
print(json.dumps(response.json(), indent=2))

# Check for a device id in the response and use it in ControlLamp.py to turn that lamp on or off