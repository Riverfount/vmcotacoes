import requests
import json


def cotar():

    req = requests.get("http://api.fixer.io/latest?base=BRL&symbols=USD,GBP,EUR,JPY")
    moeda = json.loads(req.text)

    for key in moeda['rates']:
        moeda['rates'][key] = '%.2f' % (1/moeda['rates'][key])

    return moeda

