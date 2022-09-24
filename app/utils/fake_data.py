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
    fake = Faker()
    for _ in range(upper_bound):
        sizes.append({'name': fake.word(), 'price': get_random_price(1,5)})
    return sizes


def get_random_beverages(upper_bound) -> list:
    pass
