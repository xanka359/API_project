import pytest


@pytest.fixture()
def api_url():
    return "https://petstore.swagger.io/v2/pet/"


@pytest.fixture()
def headers():
    headers = {"content-type": "application/json"}
    return headers
