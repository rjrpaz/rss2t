"""Telegram Bot API integration for sending messages to channels."""
import configparser
import re

import requests

CONFIG_INI = 'config.ini'


def cleanhtml(raw_html):
    """Strip HTML tags from a string."""
    cleanr = re.compile('<.*?>')
    return re.sub(cleanr, '', raw_html)


def send_message(tag, channel_id, link, summary):
    """Send an RSS entry as a text message to a Telegram channel."""
    config = configparser.ConfigParser()
    config.read(CONFIG_INI)

    message = '\n'.join([tag, link, cleanhtml(summary)])
    requests.get(
        f'https://api.telegram.org/bot{config["DEFAULT"]["bot_token"]}/sendMessage',
        params={'chat_id': channel_id, 'text': message},
        timeout=10,
    )
