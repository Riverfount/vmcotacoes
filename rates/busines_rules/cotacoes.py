import requests
from datetime import datetime
from rates.config import settings

API_KEY = settings.security.API_KEY  # Chave de Autenticação do Serviço


def cotar():
    # Configurações para realizar a consulta das cotações

    currencies = 'BRL, EUR, GBP, BTC'  # Moedas que serão cotadas

    # Faz a cotação na API do CurrencyLayer

    query = requests.get(f'http://apilayer.net/api/live?access_key={API_KEY}&currencies={currencies}&format=1')
    moedas = query.json()  # Converte os dados recebidos em JSON num dicionário Python

    # Se houve algum erro na consulta, retorna um dcionário com o Código e Mensagem de Erro
    if not moedas['success']:
        mensagem = {
            'sucesso': moedas['success'],
            'code': f'{moedas["error"]["code"]}',
            'info': f'{moedas["error"]["info"]}',
        }
        return mensagem

    time = datetime.fromtimestamp(moedas['timestamp'])  # Converte o Timestamp em dada em formato para humanos

    # Constrói o diconário de retorno com a data, hora e cotações do Dólar, Euro, Libra Esterlina e Biticoins

    moeda = {
        'sucesso': moedas['success'],
        'code': 200,
        'date': f'{time.day}/{time.month}/{time.year} as {time.hour}h{time.minute}min.',
        'rates': {
            'USD': f'{float(moedas["quotes"]["USDBRL"]):.2f}',
            'EUR': f'{(1 / float(moedas["quotes"]["USDEUR"])) * float(moedas["quotes"]["USDBRL"]):.2f}',
            'GBP': f'{(1 / float(moedas["quotes"]["USDGBP"])) * float(moedas["quotes"]["USDBRL"]):.2f}',
            'BTC': f'{(1 / float(moedas["quotes"]["USDBTC"])) * float(moedas["quotes"]["USDBRL"]):.2f}',
        }
    }

    return moeda
