import feedparser
import time
import signal
import sys
from rss2t import config, telegram

class TimeoutError(Exception):
    pass

def timeout_handler(_, __):
    raise TimeoutError("Operation timed out")

TIMEOUT=300
def run(timeout_seconds=TIMEOUT):
    signal.signal(signal.SIGALRM, timeout_handler)

    try:
        while True:
            signal.alarm(timeout_seconds)

            try:
                feeds = config.list_feeds()
                for feed in feeds:
                    rss_feed = feedparser.parse(feed.url)
                    # print("FEED:" + feed.url)
                    max_timestamp = 0

                    for entry in rss_feed.entries:
                        timestamp = int(time.mktime(entry.published_parsed))
                        if timestamp > int(feed.last):
                            telegram.send_message(feed.tag, feed.channel_id, entry.link, entry.summary)
                        if timestamp > max_timestamp:
                            max_timestamp = timestamp

                    feed.save_last(max_timestamp)

                signal.alarm(0)
                print("RSS processing cycle completed successfully")
                time.sleep(60)

            except TimeoutError:
                print("RSS processing timed out, continuing to next cycle...")
                signal.alarm(0)
                sys.exit(0)

    except KeyboardInterrupt:
        print("\nReceived interrupt signal, shutting down...")
        signal.alarm(0)
        sys.exit(0)


if __name__ == '__main__':
    run()
