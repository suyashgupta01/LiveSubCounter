import requests as rq
import json
import time
import os

API_KEY = '' # enter your own api key
CHANNEL_ID = 'UCt7iVnJwjBsof8IPLJHCTgQ' # enter the channel id for which subscribers are to be monitored

print("Live Subscriber Count: ")

while True:
    response = rq.get('https://www.googleapis.com/youtube/v3/channels?part=statistics&id=' + CHANNEL_ID + '&key=' + API_KEY)
    print(response.json()['items'][0]['statistics']['subscriberCount'])
    time.sleep(1)
