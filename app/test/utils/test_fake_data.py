import pytest
from app.utils.fake_data import get_random_names

def test_get_random_names():
    names = get_random_names()
    assert(len(names) == 100)