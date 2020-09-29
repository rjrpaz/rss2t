

import requests
import feedparser
import time
import json

FEED_URL = 'https://www.feedforall.com/sample.xml'

def run():
	rss_feed = feedparser.parse(FEED_URL)
	for entry in rss_feed.entries:
#		print(f"ENTRY {entry}")
		timestamp = int(time.mktime(entry.published_parsed))
		print(f"ENTRY {timestamp}")
#		send_message(str(entry))

if __name__ == '__main__':
    run()
