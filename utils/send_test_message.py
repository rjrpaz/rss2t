#!/usr/bin/env python3
"""Send a test message to a configured Telegram channel."""
import html
import sys
import configparser
import requests

CONFIG_INI = 'config.ini'

if len(sys.argv) != 2:
    print(f"Run as:\n\n\t{sys.argv[0]} <CHANNEL_TAG>\n")
    print(f"Ex:\n\n\t{sys.argv[0]} news\n")
    sys.exit(0)

channel_tag = sys.argv[1]

config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
config.read(CONFIG_INI)

if 'CHANNELS' not in config.sections():
    print("No [CHANNELS] section found in config.ini")
    sys.exit(1)

if channel_tag not in config['CHANNELS']:
    print(f"Channel '{channel_tag}' not found in [CHANNELS] section")
    print(f"Available channels: {', '.join(config['CHANNELS'].keys())}")
    sys.exit(1)

bot_token = config['DEFAULT'].get('bot_token', '')
channel_id = config['CHANNELS'][channel_tag]

message = html.unescape(f"Test message for channel '{channel_tag}'")

response = requests.get(
    f'https://api.telegram.org/bot{bot_token}/sendMessage',
    params={'chat_id': channel_id, 'text': message},
    timeout=10,
)

if response.ok and response.json().get('ok'):
    print(f"Test message sent successfully to channel '{channel_tag}' ({channel_id})")
else:
    print(f"Failed to send message to channel_id '{channel_id}': {response.text}")
    sys.exit(1)
