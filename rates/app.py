from fastapi import FastAPI, HTTPException

from rates.busines_rules.cotacoes import cotar

app = FastAPI()


@app.get('/health')
async def health():
    return {'message': 'The Api is 100% healthy.'}


@app.get('/rates')
async def rates():
    cotacoes = await cotar()
    if not cotacoes['sucesso']:
        raise HTTPException(
            status_code=cotacoes['code'],
            detail=f'{cotacoes["info"]}. Error Type: {cotacoes["type"]}'
        )
    return cotacoes
