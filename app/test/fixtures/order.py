import pytest

from ..utils.functions import (shuffle_list, get_random_sequence,
                               get_random_string)


@pytest.fixture
def order_uri():
    return '/order/'


@pytest.fixture
def order(order_mock):
    order = order_mock
    return order


@pytest.fixture
def client_data() -> dict:
    return {
        'client_address': get_random_string(),
        'client_dni': get_random_sequence(),
        'client_name': get_random_string(),
        'client_phone': get_random_sequence()
    }


@pytest.fixture
def order_mock(create_ingredients, create_sizes,
               create_beverages, client_data) -> dict:
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    beverages = [beverage.get('_id') for beverage in create_beverages]
    size_id = shuffle_list(create_sizes)[0].get('_id')
    return {
        **client_data,
        'ingredients': ingredients,
        'beverages': beverages,
        'size_id': size_id
    }


@pytest.fixture
def create_order(client, order_uri, order) -> dict:
    response = client.post(order_uri, json=order)
    return response


@pytest.fixture
def create_orders(client, order_uri, order_mock) -> list:
    orders = []
    for _ in range(10):
        new_order = client.post(order_uri, json=order_mock)
        orders.append(new_order.json)
    return orders
