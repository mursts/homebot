#!/usr/bin/env python
# coding: utf-8

import json
import urllib
import uuid

import requests
from slackbot.bot import listen_to

import slackbot_settings

ENDPOINT = 'https://todoist.com/api/v8/sync'


def add_todoist_item(content, due_date):
    commands = [{'type': 'item_add',
                 'uuid': str(uuid.uuid1()),
                 'temp_id': str(uuid.uuid1()),
                 'args': {'content': content,
                          'date_string': due_date,
                          'auto_reminder': True}}]

    payload = {'token': slackbot_settings.TODOIST_TOKEN,
               'commands': json.dumps(commands)}

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post(ENDPOINT, urllib.parse.urlencode(payload), headers=headers)

    print(r.content)
    r.raise_for_status()


@listen_to('.*振込２　オカザキジドウテアテトウ.*')
def kids_allowance(message):
    add_todoist_item('児童手当の口座振替をする', '18:05')
