import pytest
from app.test.utils.functions_seeders import (
    get_random_names, get_random_list_dni,
    get_random_addresses, get_random_phones,
    get_random_sizes, get_random_beverages,
    get_random_ingredients)

NUMBER_ORDERS = 100


def test_get_random_names():
    LANGUAGE_NAME = 'it_IT'
    names = get_random_names(LANGUAGE_NAME, NUMBER_ORDERS)
    assert(len(names) is NUMBER_ORDERS)


def test_get_random_list_dni():
    list_dni = get_random_list_dni(NUMBER_ORDERS)
    assert(len(list_dni) is NUMBER_ORDERS)


def test_get_random_addresses():
    addresses = get_random_addresses(NUMBER_ORDERS)
    assert(len(addresses) is NUMBER_ORDERS)


def test_get_random_phones():
    phones = get_random_phones(NUMBER_ORDERS)
    assert(len(phones) is NUMBER_ORDERS)


def test_get_random_sizes():
    NUMBER_SIZES = 5
    sizes = get_random_sizes(NUMBER_SIZES)
    attributes = ['name', 'price']
    for size in sizes:
        for param, value in size.items():
            pytest.assume(param in attributes)
    assert(len(sizes) is NUMBER_SIZES)


def test_get_random_beverages():
    NUMBER_BEVERAGES = 5
    beverages = get_random_beverages(NUMBER_BEVERAGES)
    attributes = ['name', 'price']
    for beverage in beverages:
        for param, value in beverage.items():
            pytest.assume(param in attributes)
    assert(len(beverages) is NUMBER_BEVERAGES)


def test_get_random_ingredients():
    NUMBER_INGREDIENTS = 13
    ingredients = get_random_ingredients(NUMBER_INGREDIENTS)
    attributes = ['name', 'price']
    for ingredient in ingredients:
        for param, value in ingredient.items():
            pytest.assume(param in attributes)
    assert(len(ingredients) is NUMBER_INGREDIENTS)
