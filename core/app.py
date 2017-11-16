from flask import Flask, render_template
from decouple import config
from core.model import model


def create_app(**kwargs):

    app = Flask('core')
    app.config["SECRET_KEY"] = config('SECRET_KEY')

    @app.route('/')
    def home():
        dicionario = model.cotar()

        if dicionario['sucesso']:
            return render_template("index.html", dicionario=dicionario)
        else:
            return render_template('error.html', dicionario=dicionario)
    return app


if __name__ == '__main__':
    app = create_app(debug=True, use_reloader=True)
    app.run(port=5000)
