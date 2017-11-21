from core.app import create_app
import pytest


@pytest.fixture()
def app():
    app = create_app()
    app.debug = True
    return app


@pytest.fixture
def instance_app():
    instance_app = create_app()
    return instance_app
