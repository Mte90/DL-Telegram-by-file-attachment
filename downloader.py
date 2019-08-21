#!/usr/bin/env python3
import configparser
import argparse
import json
from urllib.request import urlopen
import os
import re

version = '1.0.0'

parser = argparse.ArgumentParser(description='Download attachments by file names by a Telegram Channel')
parser.add_argument('--config', help='Config file', nargs='?', action='store', const='', default=os.path.abspath(os.path.dirname(__file__)) + '/config.ini')
args = parser.parse_args()

print('DL-Telegram-by-file-attachment started...')
if not os.path.exists('config.ini'):
    print('Config file not found')
    exit()

if args.config is not None:
    if not os.path.exists(args.config):
        print('Config file not found on ' + args.config)
        exit()
    print('  Config loaded!')
    config = configparser.RawConfigParser()
    config.read_file(open(args.config))

url = 'https://tg.i-c-a.su/json/' + config.get('channel', 'name') + '?limit=' + config.get('channel', 'limit')
r = urlopen(url)
data = json.loads(str(r.read().decode("utf-8")))

search = str(config.get('channel', 'filter'))
search = search.split(',')

for message in data['messages']:
    if 'media' in message:
        for term in search:
            if re.search(term, message['media']['document']['attributes'][0]['file_name'], re.IGNORECASE):
                print(' Download ' + message['media']['document']['attributes'][0]['file_name'])
                response = urlopen('https://tg.i-c-a.su/media/' + config.get('channel', 'name') + '/' + str(message['id']))
                file = open(config.get('channel', 'download') + message['media']['document']['attributes'][0]['file_name'], 'wb')
                file.write(response.read())
                file.close
