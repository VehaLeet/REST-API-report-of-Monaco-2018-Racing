import pytest
from factory import create_app

@pytest.fixture()
def app():
    app = create_app('config.Test')
    with app.app_context():
        yield app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()