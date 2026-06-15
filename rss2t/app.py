"""Main loop: fetch RSS feeds and dispatch new entries to Telegram."""
import signal
import sys
import time

import feedparser

from rss2t import config, telegram


class _RssTimeoutError(Exception):
    """Raised by the SIGALRM handler when a processing cycle exceeds the limit."""


def _timeout_handler(_, __):
    """SIGALRM handler that raises _RssTimeoutError."""
    raise _RssTimeoutError("Operation timed out")


def _process_feed(feed):
    """Fetch a single RSS feed and send any new entries to Telegram."""
    rss_feed = feedparser.parse(feed.url)
    max_timestamp = 0

    for entry in rss_feed.entries:
        timestamp = int(time.mktime(entry.published_parsed))
        if timestamp > int(feed.last):
            telegram.send_message(feed.tag, feed.channel_id, entry.link, entry.summary)
        max_timestamp = max(max_timestamp, timestamp)

    if max_timestamp > int(feed.last):
        feed.save_last(max_timestamp)


TIMEOUT = 1800


def run(timeout_seconds=TIMEOUT):
    """Poll all configured feeds once, send new entries, then exit."""
    signal.signal(signal.SIGALRM, _timeout_handler)

    try:
        while True:
            signal.alarm(timeout_seconds)
            try:
                for feed in config.list_feeds():
                    _process_feed(feed)
                signal.alarm(0)
                sys.exit(0)
            except _RssTimeoutError:
                print("RSS processing timed out, continuing to next cycle...")
                signal.alarm(0)
                sys.exit(0)
    except KeyboardInterrupt:
        print("\nReceived interrupt signal, shutting down...")
        signal.alarm(0)
        sys.exit(0)


if __name__ == '__main__':
    run()
