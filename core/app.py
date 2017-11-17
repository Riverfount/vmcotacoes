import os

from decouple import config
from flask import Flask, render_template

from core.model import cotacoes


def create_app():

    app = Flask('core')
    app.config["SECRET_KEY"] = config('SECRET_KEY')

    @app.route('/')
    def home():
        dicionario = cotacoes.cotar()

        if dicionario['sucesso']:
            return render_template("index.html", dicionario=dicionario)
        else:
            return render_template('error.html', dicionario=dicionario)
    return app


if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
