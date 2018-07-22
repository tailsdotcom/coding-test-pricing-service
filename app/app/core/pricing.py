import json
import os

DIR = os.path.dirname(os.path.abspath(__file__))
FILE_LOCATION = os.path.join(DIR, 'pricing.json')


def get_price_rules():

    with open(FILE_LOCATION) as f:
        rules = json.load(f)

    prices = {}
    for p in rules['prices']:
        id = p['product_id']
        price = p['price']
        vat_band = p['vat_band']
        prices[id] = {
            'price' : price,
            'vat_band': vat_band
        }

    vat_rates = rules['vat_bands']

    return prices, vat_rates
