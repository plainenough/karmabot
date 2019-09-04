from collections import Counter
import logging
import os
import pickle
import re
import sys
import yaml
from slackclient import SlackClient
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s' +
                    ' %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='data/slackbot.log')
try:
    with open('data/config.yaml', 'r') as _config:
        config = yaml.load(_config.read())
        logging.info('Valid config found')
except FileNotFoundError:
    logging.info('no config found')
    from utils.create_config import TEMPLATE, create_config
    logging.info('creating config')
    create_config()
except yaml.scanner.ScannerError as e:
    logging.info('Config has invalid format')
    logging.debug(e)
    sys.exit(1)
if 'BOTNAME' in config:
    logging.info('Grabbing botname from config')
    botuser = config['BOTNAME']
else:
    botuser = os.environ.get('SLACK_KARMA_BOTUSER')
if 'SLACK_KARMA_TOKEN' in config:
    logging.info('grabbing slack token from config')
    token = config['SLACK_KARMA_TOKEN']
else:
    token = os.environ.get('SLACK_KARMA_TOKEN')
if not botuser or not token:
    logging.info('Make sure you set SLACK_KARMA_BOTUSER' +
                 'SLACK_KARMA_TOKEN in env and config')
    sys.exit(1)
KARMA_BOT = botuser
SLACK_CLIENT = SlackClient(token)
MAX_POINTS = 5
# the first +/- is merely signaling, start counting (regex capture)
# from second +/- onwards, so bob++ adds 1 point, bob+++ = +2, etc
KARMA_ACTION = re.compile(r'(?:^| )(\S{2,}?)\s?[\+\-]([\+\-]+)')
IS_USER = re.compile(r'^<@[^>]+>$')
USERNAME_CACHE = {}
KARMA_CACHE = 'data/score'
CONFIG = config
logging.info('Script started')
try:
    logging.info('Retrieving karma cache file')
    karmas = pickle.load(open(KARMA_CACHE, "rb"))
except FileNotFoundError:
    logging.info('No cache file starting new Counter object in memory')
    karmas = Counter()
