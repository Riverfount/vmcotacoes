import vcr
import yaml
from flask import url_for

from core.model.cotacoes import cotar

# VCRPY Set up
my_vcr = vcr.VCR(filter_query_parameters=['access_key'],
                 cassette_library_dir='tests/fixtures/vcr_cassettes',
                 record_mode='once',
                 match_on=['url', ])


def test_app_exists(instance_app):
    assert instance_app.name == 'core'


def test_app_static_folder(instance_app):
    assert instance_app.has_static_folder


def test_app_template_folder(instance_app):
    assert instance_app.template_folder


@my_vcr.use_cassette('data_success.yaml')
def test_app_status_code(client):
    assert client.get(url_for('home')).status_code == 200


@my_vcr.use_cassette('data_success.yaml')
def test_api_data_success():
    data_success = cotar()
    with open('tests/fixtures/vcr_cassettes/data_success.yaml', 'r') as f:
        assert yaml.load(f)['interactions'][0]['response']['status']['code'] == data_success['code']
