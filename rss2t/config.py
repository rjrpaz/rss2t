import logging
import configparser
from configparser import ConfigParser, ExtendedInterpolation

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.disabled = True

config_ini = 'config.ini'

class Feed(object):
    def __init__(self):
        self.tag = None
        self.last = 0
        self.url = ''
        self.channel_id = ''

    def save_last(self, last):
        logger.info(f"Storing timestamp {last} for tag {self.tag}")
        config = configparser.ConfigParser()
        config.read(config_ini)

        config.set(self.tag, 'last', str(last))
        with open(config_ini, 'w') as configfile:
            config.write(configfile, True)
        del config

def list_feeds():
    feeds = []
    config = configparser.ConfigParser(interpolation=ExtendedInterpolation())
    config.read(config_ini)
    sections = config.sections()
    for section in sections:
        if section == 'CHANNELS':
            continue

        feed = Feed()
        feed.tag = section
        logger.info(f"Procesing section {section}")
        try:
            feed.url = config[section]['url']
        except:
            print(f"Section {section} don't have url")
        try:
            feed.channel_id = config[section]['channel_id']
        except:
            print(f"Section {section} don't have channel_id")
        if not config[section]['last']:
            feed.last = 0
        else:
            feed.last = config[section]['last']
        feeds.append(feed)
    
    del config

    return feeds
