import pytest
from app.utils.fake_data import get_random_names


def test_get_random_names():
    LANGUAGE_NAME = 'it_IT'
    UPPER_BOUNDER = 100
    names = get_random_names(LANGUAGE_NAME, UPPER_BOUNDER)
    assert(len(names) is UPPER_BOUNDER)
