#!/usr/bin/env python
# coding: utf-8

import requests
from slackbot.bot import respond_to, listen_to

import slackbot_settings


@respond_to('こんにちは')
def cheer(message):
    message.reply('はろー')


@listen_to('help')
def help(message):
    message.send('May I help you?')


@listen_to('googlehome (.*)')
def to_googlehome(message, say):
    url = slackbot_settings.GOOGLE_HOME_NOTIFIER_URL
    payload = {'text': say}
    requests.post(url, payload)
