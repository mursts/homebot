#!/usr/bin/env python
# coding: utf-8

import requests
from slackbot.bot import listen_to

import slackbot_settings

GEO_API_ENDPOINT = 'https://map.yahooapis.jp/geocode/V1/geoCoder'
STATIC_MAP_API_ENDPOINT = 'https://map.yahooapis.jp/map/V1/static'


def get_coordinates(query):
    params = {'appid': slackbot_settings.YAHOO_APP_ID,
              'query': query,
              'results': 1,
              'output': 'json'}

    r = requests.get(GEO_API_ENDPOINT, params=params)
    return r.json()['Feature'][0]['Geometry']['Coordinates'].split(',')


def get_rain_fall_image(lon, lat):
    params = {'appid': slackbot_settings.YAHOO_APP_ID,
              'lon': lon,
              'lat': lat,
              'mode': 'map',
              'z': 15,
              'overlay': 'type:rainfall|datelabel:on'}
    r = requests.get(STATIC_MAP_API_ENDPOINT, params=params)
    return r.content


@listen_to('雨 (.*)')
def rail_fall(message, query):
    try:
        lon, lat = get_coordinates(query)
        map_content = get_rain_fall_image(lon, lat)
        with open('rain_fall.png', 'wb') as f:
            f.write(map_content)
        message.channel.upload_file('rain_fall.png', 'rain_fall.png')
    except TypeError as e:
        print(e)
