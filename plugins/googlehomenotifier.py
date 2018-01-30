#!/usr/bin/env python
# coding: utf-8

import requests
from slackbot.bot import respond_to, listen_to


@respond_to('こんにちは')
def cheer(message):
    message.reply('はろー')


@listen_to('help')
def help(message):
    message.send('May I help you?')


@listen_to('googlehome (.*)')
def to_googlehome(message, say):
    url = 'http://localhost:8089/google-home-notifier'
    payload = {'text': say}
    requests.post(url, payload)
