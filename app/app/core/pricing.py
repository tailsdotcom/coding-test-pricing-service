import json
import os

DIR = os.path.dirname(os.path.abspath(__file__))
FILE_LOCATION = os.path.join(DIR, 'pricing.json')


def get_price_rules():

    with open(FILE_LOCATION) as f:
        rules = json.load(f)
    return rules
