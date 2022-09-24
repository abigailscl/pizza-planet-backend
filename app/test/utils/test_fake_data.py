import pytest
from faker import Faker

def test_get_random_names() -> str:
    names = get_random_names()
    assert(len(names) == 100)