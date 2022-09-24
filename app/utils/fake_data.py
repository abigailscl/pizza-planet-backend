from faker import Faker
from app.test.utils.functions import get_random_price


def get_random_names(language_name, upper_bound) -> list:
    name = []
    fake = Faker(language_name)
    for _ in range(upper_bound):
        name.append(fake.name())
    return name


def get_random_list_dni(upper_bound) -> list:
    list_dni = []
    fake = Faker()
    for _ in range(upper_bound):
        list_dni.append(fake.ssn())
    return list_dni


def get_random_addresses(upper_bound) -> list:
    addresses = []
    fake = Faker()
    for _ in range(upper_bound):
        addresses.append(fake.address())
    return addresses


def get_random_phones(upper_bound) -> list:
    phones = []
    fake = Faker()
    for _ in range(upper_bound):
        phones.append(fake.phone_number())
    return phones


def get_random_sizes(upper_bound) -> list:
    sizes = []
    MINIMUM_PRICE = 1
    MAXIMUM_PRICE = 5

    fake = Faker()
    for _ in range(upper_bound):
        sizes.append({'name': fake.word(),
                      'price': get_random_price(MINIMUM_PRICE, MAXIMUM_PRICE)})
    return sizes


def get_random_beverages(upper_bound) -> list:
    beverages = []
    MINIMUM_PRICE = 1
    MAXIMUM_PRICE = 5

    fake = Faker()
    for _ in range(upper_bound):
        beverages.append({'name': fake.word(),
                          'price': get_random_price(
                            MINIMUM_PRICE, MAXIMUM_PRICE)})
    return beverages


def get_random_ingredients(upper_bound) -> list:
    ingredients = []
    MINIMUM_PRICE = 1
    MAXIMUM_PRICE = 5

    fake = Faker()
    for _ in range(upper_bound):
        ingredients.append({'name': fake.word(),
                            'price': get_random_price(
                                MINIMUM_PRICE, MAXIMUM_PRICE)})
    return ingredients
