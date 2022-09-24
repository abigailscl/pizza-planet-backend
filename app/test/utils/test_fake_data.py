import pytest

def test_get_random_names():
    names = get_random_names()
    assert(len(names) == 100)