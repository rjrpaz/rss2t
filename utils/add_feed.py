#!/usr/bin/env python3
import sys
import configparser

config_ini = 'config.ini'

if len(sys.argv) != 3:
    print(f"Run as:\n\n\t{sys.argv[0]} <TAG> <URL>\n\n")
    print(f"Ex:\n\n\t{sys.argv[0]} RESTAURANT https://www.feedforall.com/sample.xml\n\n")
    exit(0)

tag = sys.argv[1]
url = sys.argv[2]

config = configparser.ConfigParser()
config.read(config_ini)

if tag in config.sections():
    print(f"Tag {tag} already exist!")
    exit(1)

config[tag] = {}
config[tag]['last'] = '0'
config[tag]['url'] = url

with open(config_ini, 'w') as configfile:
    config.write(configfile)
