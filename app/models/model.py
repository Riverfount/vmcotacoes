from yahoo_finance import Currency
from datetime import datetime


def cotar():

    usd_brl, eur_brl, gbp_brl, jpy_brl = Currency('USDBRL'), Currency('EURBRL'), Currency('GBPBRL'), Currency('JPYBRL')

    data = datetime.strptime(usd_brl.get_trade_datetime()[:-9], '%Y-%m-%d %H:%M:%S')
    data = datetime.strftime(data, '%d/%m/%Y')


    moeda = {
        'base': 'BRL',
        'date': data,
        'rates': {
            'GBP': f'{float(gbp_brl.get_ask()):.2f}',
            'JPY': f'{float(jpy_brl.get_ask()):.2f}',
            'USD': f'{float(usd_brl.get_ask()):.2f}',
            'EUR': f'{float(eur_brl.get_ask()):.2f}'
        }
    }

    return moeda
