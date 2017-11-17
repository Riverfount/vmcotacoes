import pytest
from flask import url_for

from core.app import create_app


@pytest.fixture
def instance_app():
    instance_app = create_app()
    return instance_app


def test_app_exists(instance_app):
    assert instance_app.name == 'core'


def test_app_static_folder(instance_app):
    assert instance_app.has_static_folder


def test_template_folder(instance_app):
    assert instance_app.template_folder


def test_status_code(client):
    assert client.get(url_for('home')).status_code == 200


def test_status_code_apilayer(mocker):
    request_mock = mocker.patch('core.model.cotacoes.cotar')
    assert request_mock.get.return_value.status_code == 200