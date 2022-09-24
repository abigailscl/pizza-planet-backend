import pytest
from app.utils.fake_data import get_random_names

def test_get_random_names():
    UPPER_BOUNDER = 100
    names = get_random_names(UPPER_BOUNDER)
    assert(len(names) == UPPER_BOUNDER)