import requests
import os

try:
    requests.get('https://google.com')
except:
    os.system('systemctl restart wg-quick@wg0.service')
