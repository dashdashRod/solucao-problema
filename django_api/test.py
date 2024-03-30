import requests
import json

URL = 'https://127.0.0.1:8000/home/'

response = requests.get(url=URL)

print(response.text)