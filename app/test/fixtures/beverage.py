import pytest

from ..utils.functions import get_random_price, get_random_string


def beverage_mock() -> dict:
    return {
        'name': get_random_string(),
        'price': get_random_price(10, 20)
    }


@pytest.fixture
def beverage_uri():
    return '/beverage/'


@pytest.fixture
def beverage():
    return beverage_mock()


@pytest.fixture
def beverages():
    NUMBER_BEVERAGES = 5
    return [beverage_mock() for _ in range(NUMBER_BEVERAGES)]


@pytest.fixture
def create_beverage(client, beverage_uri) -> dict:
    response = client.post(beverage_uri, json=beverage_mock())
    return response


@pytest.fixture
def create_beverages(client, beverage_uri) -> list:
    NUMBER_BEVERAGES = 10
    beverages = []
    for _ in range(NUMBER_BEVERAGES):
        new_beverage = client.post(beverage_uri, json=beverage_mock())
        beverages.append(new_beverage.json)
    return beverages
