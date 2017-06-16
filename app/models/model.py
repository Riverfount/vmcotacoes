from yahoo_finance import Currency


def cotar():

    usd_brl = Currency('USDBRL')
    eur_brl = Currency('EURBRL')
    gbp_brl = Currency('GBPBRL')
    jpy_brl = Currency('JPYBRL')

    usd_data = usd_brl.get_trade_datetime()[:10]

    moeda = {
        'base': 'BRL',
        'date': usd_data,
        'rates': {
            'GBP': f'{float(gbp_brl.get_ask()):.2f}',
            'JPY': f'{float(jpy_brl.get_ask()):.2f}',
            'USD': f'{float(usd_brl.get_ask()):.2f}',
            'EUR': f'{float(eur_brl.get_ask()):.2f}'
        }
    }

    return moeda
