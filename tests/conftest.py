import pytest

from webtagger_service.application import application


@pytest.fixture
def client():
    application.config['TESTING'] = True
    yield application.test_client()
