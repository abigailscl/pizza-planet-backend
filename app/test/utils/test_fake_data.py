import pytest
from app.utils.fake_data import (get_random_names, get_random_list_dni,
                                 get_random_addresses, get_random_phones,
                                 get_random_sizes)


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

def test_get_random_phones():
    NUMBER_SIZES = 100
    sizes = get_random_sizes(NUMBER_SIZES)
    assert(len(sizes) is NUMBER_SIZES)
