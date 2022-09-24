from faker import Faker

def get_random_names():
    name = []
    fake = Faker('it_IT')
    for _ in range(100):
        name.append(fake.name())
    return name
