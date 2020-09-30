import logging
import configparser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.disabled = True

config_ini = 'config.ini'

class Feed(object):
    def __init__(self):
        self.tag = None
        self.last = 0
        self.url = ''

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
    config = configparser.ConfigParser()
    config.read(config_ini)
    sections = config.sections()
    for section in sections:
        feed = Feed()
        feed.tag = section
        logger.info(f"Procesing section {section}")
        try:
            feed.url = config[section]['url']
        except:
            print(f"Section {section} don't have url")
        if not config[section]['last']:
            feed.last = 0
        else:
            feed.last = config[section]['last']
        feeds.append(feed)
    
    del config

    return feeds
