import requests
import html
from rss2t.local_settings import bot_token, channel_id
import re

def cleanhtml(raw_html):
	cleanr = re.compile('<.*?>')
	cleantext = re.sub(cleanr, '', raw_html)
	return cleantext

def send_message(link, summary):
	message = '\n'.join([link, cleanhtml(summary)])
	requests.get(f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={channel_id}&text={message}')
