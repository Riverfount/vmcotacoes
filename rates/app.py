from flask import Flask, render_template

from rates.busines_rules import cotacoes


def create_app():
    app = Flask('core')

    @app.route('/')
    def home():
        dicionario = cotacoes.cotar()

        if dicionario['sucesso']:
            template_renderised = render_template("index.html", dicionario=dicionario)
        else:
            template_renderised = render_template('error.html', dicionario=dicionario)

        return template_renderised

    return app
