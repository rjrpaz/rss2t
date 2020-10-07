import requests
import html
import re
import configparser

config_ini = 'config.ini'

def cleanhtml(raw_html):
	cleanr = re.compile('<.*?>')
	cleantext = re.sub(cleanr, '', raw_html)
	return cleantext

def send_message(tag, link, summary):
	config = configparser.ConfigParser()
	config.read(config_ini)

	message = '\n'.join([tag,link, cleanhtml(summary)])
#	print (message)
	requests.get(f'https://api.telegram.org/bot{config["DEFAULT"]["bot_token"]}/sendMessage?chat_id={config["DEFAULT"]["channel_id"]}&text={message}')
