from faker import Faker


def get_random_names(language_name, upper_bpund) -> list:
    name = []
    fake = Faker(language_name)
    for _ in range(upper_bpund):
        name.append(fake.name())
    return name
