import pytest

from app.test.utils.functions import get_random_string, get_random_price


def test_create_order_service(create_order):
    order = create_order.json
    pytest.assume(create_order.status.startswith('200'))
    pytest.assume(order['_id'])
    pytest.assume(order['name'])
    pytest.assume(order['price'])


def test_update_order_service(client, create_order, order_uri):
    UPPER_BOUND_PRICE = 5
    LOWER_BOUND_PRICE = 1
    current_order = create_order.json
    update_data = {**current_order, 'name': get_random_string(),
                   'price': get_random_price(LOWER_BOUND_PRICE,
                                             UPPER_BOUND_PRICE)}
    response = client.put(order_uri, json=update_data)
    pytest.assume(response.status.startswith('200'))
    updated_order = response.json
    for param, value in update_data.items():
        pytest.assume(updated_order[param] == value)


def test_get_order_by_id_service(client, create_order, order_uri):
    current_order = create_order.json
    response = client.get(f'{order_uri}id/{current_order["_id"]}')
    pytest.assume(response.status.startswith('200'))
    returned_order = response.json
    for param, value in current_order.items():
        pytest.assume(returned_order[param] == value)


def test_get_orders_service(client, create_orders, order_uri):
    response = client.get(order_uri)
    print(response)
    pytest.assume(response.status.startswith('308'))
    returned_order = {order['_id']: order for order in response.json}
    for order in create_orders:
        pytest.assume(order['_id'] in returned_order)
