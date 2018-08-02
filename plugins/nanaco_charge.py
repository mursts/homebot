#!/usr/bin/env python
# coding: utf-8

import slackbot_settings
from pynanacolight import Nanaco
from slackbot.bot import respond_to


@respond_to('nanaco charge (.*)')
@respond_to('nanaco チャージ (.*)')
def charge(message, amount):
    try:
        amount = int(amount)
    except ValueError:
        message.send('数字を入れましょう')
        return

    if amount < 5000:
        message.send('金額は5000円以上')
        return

    mynanaco = Nanaco()
    mynanaco.login(slackbot_settings.NANACO_NUMBER, slackbot_settings.CARD_NUMBER)
    mynanaco.login_credit_charge(slackbot_settings.CREDIT_CHARGE_PASSWORD)
    mynanaco.charge(amount)

    message.react('ok')


@respond_to('nanaco now')
def charge(message):
    mynanaco = Nanaco()
    mynanaco.login(slackbot_settings.NANACO_NUMBER, slackbot_settings.CARD_NUMBER)
    msg = '{:,d}円 (センター{:,d}円)'.format(int(mynanaco.balance_card), int(mynanaco.balance_center))
    message.send(msg)
