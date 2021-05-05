#!/usr/bin/env python

import os
import requests
import flask

app = flask.Flask(__name__)

INVESTMENT = 22538.09

path = os.path.expanduser('~/.eth_addresses')
with open(path) as f:
    ADDRESSES = [a.strip() for a in f.read().splitlines() if not a.strip().startswith('#') and a.strip()]

def get_usd_price(asset):
    response = requests.get('https://api.coinmarketcap.com/v1/ticker/{0}/'.format(asset))
    data =response.json()
    return float(data[0]['price_usd'])

def get_total(addresses):
    headers = {'Content-Type': 'application/json'}
    total = 0
    for address in addresses:
        params = {'jsonrpc': '2.0', 'method': 'eth_getBalance', 'params': [address, 'latest'], 'id': 1}
        response = requests.get('http://127.0.0.1:8545', json=params)
        print response.json()
        total += int(response.json()['result'], base=16) / 1000000000000000000.0
    return total


def get_ripple_total():
    response = requests.get('https://data.ripple.com/v2/accounts/r9wr5vA9WpXNmqiqK2hSoWGtuFM7kZq9pW/balances')
    balance, = response.json()['balances']
    value = float(balance['value'])
    return value

@app.route('/')
def index():
    total_eth = get_total(ADDRESSES) * get_usd_price('ethereum')
    total_xrp = get_ripple_total() * get_usd_price('ripple')
    lines = [
        'total eth: {0}'.format(total_eth),
        'total xrp: {0}'.format(total_xrp),
        '',
        'GRAND TOTAL: {0}'.format(total_eth + total_xrp),
        '',
        'invested: {0}'.format(INVESTMENT),
        # (final - initial) / initial * 100
        '% return: {0}'.format((total_eth + total_xrp - INVESTMENT) / INVESTMENT * 100)
    ]
    text = '\n'.join(lines)
    return flask.Response(text, mimetype='text/plain')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=27352)

