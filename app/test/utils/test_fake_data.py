import pytest
from app.utils.fake_data import (get_random_names, get_random_list_dni,
                                 get_random_addresses, get_random_phones,
                                 get_random_sizes, get_random_beverages,
                                 get_random_ingredients)


def test_get_random_names():
    LANGUAGE_NAME = 'it_IT'
    NUMBER_NAMES = 100
    names = get_random_names(LANGUAGE_NAME, NUMBER_NAMES)
    assert(len(names) is NUMBER_NAMES)


def test_get_random_list_dni():
    NUMBER_DNI = 100
    list_dni = get_random_list_dni(NUMBER_DNI)
    assert(len(list_dni) is NUMBER_DNI)


def test_get_random_addresses():
    NUMBER_ADDRESSES = 100
    addresses = get_random_addresses(NUMBER_ADDRESSES)
    assert(len(addresses) is NUMBER_ADDRESSES)


def test_get_random_phones():
    NUMBER_PHONES = 100
    phones = get_random_phones(NUMBER_PHONES)
    assert(len(phones) is NUMBER_PHONES)


def test_get_random_sizes():
    NUMBER_SIZES = 5
    sizes = get_random_sizes(NUMBER_SIZES)
    attributes = ['name', 'price']
    for size in sizes:
        for param, value in size.items():
            pytest.assume(param in attributes)
    assert(len(sizes) is NUMBER_SIZES)


def test_get_random_beverages():
    NUMBER_BEVERAGES = 10
    beverages = get_random_beverages(NUMBER_BEVERAGES)
    attributes = ['name', 'price']
    for beverage in beverages:
        for param, value in beverage.items():
            pytest.assume(param in attributes)
    assert(len(beverages) is NUMBER_BEVERAGES)


def test_get_random_ingredients():
    NUMBER_INGREDIENTS = 10
    ingredients = get_random_ingredients(NUMBER_INGREDIENTS)
    attributes = ['name', 'price']
    for ingredient in ingredients:
        for param, value in ingredient.items():
            pytest.assume(param in attributes)
    assert(len(ingredients) is NUMBER_INGREDIENTS)
