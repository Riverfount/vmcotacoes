import vcr
from flask import url_for
from core.model.cotacoes import cotar

# Tests about the app instantiation


def test_app_exists(instance_app):
    assert instance_app.name == 'core'


def test_app_static_folder(instance_app):
    assert instance_app.has_static_folder


def test_app_template_folder(instance_app):
    assert instance_app.template_folder


def test_app_status_code(client):
    assert client.get(url_for('home')).status_code == 200

# Test about the result of app


@vcr.use_cassette('tests/fixtures/vcr_cassettes/data_success.yaml')
def test_api_data_success():
    data_success = cotar()
    assert data_success  # Teste besta só exemplo
