from faker import Faker


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
