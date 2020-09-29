import requests
import feedparser
import time
import json

FEED_URL = 'https://www.feedforall.com/sample.xml'


def send_message(entry):
#	print(json.dumps(entry, indent=4, sort_keys=True))
#	json_data = json.loads(entry)[0]
#	print("%s" % (entry['title']))
#	print(type(entry))
	entry = entry.replace("\'", "\"")
	entry = entry.replace(": None", ": \"None\"")
	entry = entry[:389]
	print(entry)
	parsed_json = json.loads(entry)
#	print(type(parsed_json))
	print (parsed_json["title"])
#        requests.get(f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHANNEL_ID}&text={message}')
