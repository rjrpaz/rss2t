"""Configuration loader and feed state manager for rss2t."""
import configparser
from configparser import ExtendedInterpolation
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.disabled = True

CONFIG_INI = 'config.ini'


class Feed:  # pylint: disable=too-few-public-methods
    """Represents a single RSS feed entry from config.ini."""

    def __init__(self):
        """Initialise with empty/default values."""
        self.tag = None
        self.last = 0
        self.url = ''
        self.channel_id = ''

    def save_last(self, last):
        """Persist the latest seen timestamp back to config.ini."""
        logger.info("Storing timestamp %s for tag %s", last, self.tag)
        config = configparser.ConfigParser()
        try:
            config.read(CONFIG_INI)
            config.set(self.tag, 'last', str(last))
            with open(CONFIG_INI, 'w', encoding='utf-8') as configfile:
                config.write(configfile, True)
                configfile.flush()
        except (OSError, configparser.Error) as exc:
            logger.error("Error saving timestamp for %s: %s", self.tag, exc)
        finally:
            del config


def list_feeds():
    """Read config.ini and return a list of Feed objects."""
    feeds = []
    config = configparser.ConfigParser(interpolation=ExtendedInterpolation())
    try:
        config.read(CONFIG_INI)
        for section in config.sections():
            if section == 'CHANNELS':
                continue

            feed = Feed()
            feed.tag = section
            logger.info("Procesing section %s", section)
            try:
                feed.url = config[section]['url']
            except KeyError:
                print(f"Section {section} don't have url")
            try:
                feed.channel_id = config[section]['channel_id']
            except KeyError:
                print(f"Section {section} don't have channel_id")
            feed.last = config[section].get('last', '0') or '0'
            feeds.append(feed)
    except configparser.Error as exc:
        logger.error("Error reading configuration: %s", exc)
    finally:
        del config

    return feeds
