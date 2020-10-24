#!/usr/bin/env python3
import sys
import configparser

config_ini = 'config.ini'

if len(sys.argv) != 4:
    print(f"Run as:\n\n\t{sys.argv[0]} <TAG> <CHANNEL_TAG> <URL>\n\n")
    print(f"Ex:\n\n\t{sys.argv[0]} RESTAURANT entertainment https://www.feedforall.com/sample.xml\n\n")
    exit(0)

tag = sys.argv[1]
channel = sys.argv[2]
url = sys.argv[3]

config = configparser.ConfigParser()
config.read(config_ini)

if tag in config.sections():
    print(f"Tag {tag} already exist!")
    exit(1)

try:
    feed.channel_id = config['CHANNELS'][channel]
except:
    print(f"Channel {channel} not included in the 'CHANNELS' section")


config[tag] = {}
config[tag]['last'] = '0'
config[tag]['url'] = url
config[tag]['channel_id'] = '${CHANNELS:' + channel + '}'

with open(config_ini, 'w') as configfile:
    config.write(configfile)
