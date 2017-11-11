from app import app
from app.models import model
from bottle import template
from bottle import static_file


# Static Routes


@app.get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='app/static/css')


@app.get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='app/static/js')


@app.get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='app/static/img')


@app.get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='app/static/fonts')


@app.route('/')
def index():
    dicionario = model.cotar()

    if dicionario['sucesso']:
        return template("cotacao", dicionario=dicionario)
    else:
        return template('error', dicionario=dicionario)




