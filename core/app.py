from core.model import cotacoes
from flask import Flask, render_template

from .config import settings


def create_app():
    app = Flask('core')
    app.config["SECRET_KEY"] = settings.SECRET_KEY

    @app.route('/')
    def home():
        dicionario = cotacoes.cotar()

        if dicionario['sucesso']:
            template_renderised = render_template("index.html", dicionario=dicionario)
        else:
            template_renderised = render_template('error.html', dicionario=dicionario)

        return template_renderised

    return app
