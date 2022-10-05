from unittest.mock import patch

from flask import url_for


def test_app_exists(instance_app):
    assert instance_app.name == 'core'


def test_app_static_folder(instance_app):
    assert instance_app.has_static_folder


def test_app_template_folder(instance_app):
    assert instance_app.template_folder


@patch('core.app.cotacoes.cotar')
def test_app_status_code_200_ok(mock_cotar, client):
    mock_cotar.return_value = {
        'sucesso': True,
        'code': 200,
        'date': '05/10/2022 as 12h03min.',
        'rates': {
            'USD': '5.23',
            'EUR': '1.01',
            'GBP': '0.88',
            'BTC': '5.02',
        }
    }
    response = client.get(url_for('home'))
    assert response.status_code == 200
    assert 'Cotado a: <span class="bg-success">R$ 5.23</span>' in response.text
    assert 'Última consulta em 05/10/2022 as 12h03min.' in response.text
