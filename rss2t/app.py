import requests
import feedparser
import time
from rss2t import config, telegram

def run():
	feeds = config.list_feeds()
	for feed in feeds:
		rss_feed = feedparser.parse(feed.url)
		max_timestamp = 0

		for entry in rss_feed.entries:
			timestamp = int(time.mktime(entry.published_parsed))
			if timestamp > int(feed.last):
				telegram.send_message(feed.tag, entry.link, entry.summary)
			if timestamp > max_timestamp:
				max_timestamp = timestamp

		feed.save_last(max_timestamp)

if __name__ == '__main__':
    run()
