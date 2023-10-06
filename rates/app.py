from fastapi import FastAPI

app = FastAPI()


@app.get('/health')
def health():
    return {'message': 'The Api is 100% healthy.'}
