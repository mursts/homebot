import os

API_TOKEN = os.environ.get('API_TOKEN', '')

DEFAULT_REPLY = os.environ.get('DEFAULT_REPLY', '')
ERRORS_TO = os.environ.get('ERRORS_TO', '')

PLUGINS = [
    'plugins',
]

YAHOO_APP_ID = os.environ.get('YAHOO_APP_ID', '')

TODOIST_TOKEN = os.environ.get('TODOIST_TOKEN', '')

# nanaco
NANACO_NUMBER = os.environ.get('NANACO_NUMBER', '')
CARD_NUMBER = os.environ.get('CARD_NUMBER', '')
CREDIT_CHARGE_PASSWORD = os.environ.get('CREDIT_CHARGE_PASSWORD', '')
