from faker import Faker

def get_random_names(upper_bpund):
    name = []
    fake = Faker('it_IT')
    for _ in range(upper_bpund):
        name.append(fake.name())
    return name
