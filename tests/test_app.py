from flask import url_for

from core.app import create_app


def test_app_exists():
    resp = create_app()
    assert resp.name == 'core'


def test_app_static_folder():
    resp = create_app()
    assert resp.has_static_folder


def test_template_folder():
    resp = create_app()
    assert resp.template_folder


def test_status_code(client):
    resp = client.get(url_for('home'))
    assert resp.status_code == 200
