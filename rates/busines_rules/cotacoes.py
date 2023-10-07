from fastapi import HTTPException
import httpx
from datetime import datetime
from rates.config import settings
from pydantic import BaseModel

API_KEY = settings.security.API_KEY  # Chave de Autenticação do Serviço


# Models

class RateResponseOk(BaseModel):
    date: datetime


async def cotar():
    # Configurações para realizar a consulta das cotações

    currencies = 'BRL, EUR, GBP, BTC'  # Moedas que serão cotadas

    # Faz a cotação na API do CurrencyLayer

    async with httpx.AsyncClient() as client:
        query = await client.get(
            f'http://apilayer.net/api/live?access_key={API_KEY}&currencies={currencies}&source=USD&format=1',
            timeout=10
        )

    rates = query.json()  # Converte os dados recebidos em JSON num dicionário Python

    # Se houve algum erro na consulta, retorna um dcionário com o Código e Mensagem de Erro
    if not rates['success']:
        moedas = {
            'sucesso': rates['success'],
            'code': rates['error']['code'],
            'info': rates['error']['info'],
            'type': rates['error']['type']
        }
    else:
        moedas = {
            'sucesso': rates['success'],
            'timestamp': rates['timestamp'],
            'rates': {
                'USD': f'{float(rates["quotes"]["USDBRL"]):.2f}',
                'EUR': f'{(1 / float(rates["quotes"]["USDEUR"])) * float(rates["quotes"]["USDBRL"]):.2f}',
                'GBP': f'{(1 / float(rates["quotes"]["USDGBP"])) * float(rates["quotes"]["USDBRL"]):.2f}',
                'BTC': f'{(1 / float(rates["quotes"]["USDBTC"])) * float(rates["quotes"]["USDBRL"]):.2f}',
            }
        }

    return moedas
