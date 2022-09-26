from faker import Faker

MINIMUM_PRICE = 1
MAXIMUM_PRICE = 5

FAKE_BEVERAGES = [
    {'name': 'Pepsi', 'price': 1.10},
    {'name': 'Fioravanti', 'price': 1.10},
    {'name': 'Water', 'price': 1},
    {'name': 'Sprite', 'price': 2},
    {'name': 'Natural juice', 'price': 2.80},
]

FAKE_SIZES = [
    {'name': 'Little', 'price': 4.99},
    {'name': 'Personal', 'price': 6.99},
    {'name': 'Medium', 'price': 8.99},
    {'name': 'Family', 'price': 12.99},
    {'name': 'Big', 'price': 23.99},
]

FAKE_INGREDIENTS = [
    {'name': 'Salami', 'price': 2.25},
    {'name': 'Cheese', 'price': 2.55},
    {'name': 'Pineaple', 'price': 2.10},
    {'name': 'Pepperoni', 'price': 2.25},
    {'name': 'Bacon', 'price': 2.25},
    {'name': 'Meet', 'price': 2.10},
    {'name': 'Ham', 'price': 2.25},
    {'name': 'Sausage', 'price': 2.10},
    {'name': 'Onion', 'price': 1.10},
    {'name': 'Olives', 'price': 1.10},
    {'name': 'Tomato', 'price': 1.10},
    {'name': 'Oregano', 'price': 0.50},
    {'name': 'Mushroom', 'price': 1.10},
]


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

    if len(FAKE_SIZES) is not upper_bound:
        return FAKE_SIZES

    for _ in range(upper_bound):
        sizes.append(FAKE_SIZES[_])
    return sizes


def get_random_beverages(upper_bound) -> list:
    beverages = []

    if len(FAKE_BEVERAGES) is not upper_bound:
        return FAKE_BEVERAGES

    for _ in range(upper_bound):
        beverages.append(FAKE_BEVERAGES[_])
    return beverages


def get_random_ingredients(upper_bound) -> list:
    ingredients = []

    if len(FAKE_INGREDIENTS) is not upper_bound:
        return FAKE_INGREDIENTS

    for _ in range(upper_bound):
        ingredients.append(FAKE_INGREDIENTS[_])
    return ingredients
