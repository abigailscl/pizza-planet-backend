import random
import string
from random import sample
from typing import Any, Union


def get_random_string() -> str:
    letters = list(string.ascii_lowercase)
    random.shuffle(letters)
    return ''.join(letters[:10])


def get_random_choice(choices: Union[tuple, list]) -> Any:
    return random.choice(choices)


def get_random_price(lower_bound: float, upper_bound: float) -> float:
    NUMBER_DIGITS = 2
    return round(random.uniform(lower_bound, upper_bound), NUMBER_DIGITS)


def shuffle_list(choices: list) -> list:
    choice_copy = choices.copy()
    random.shuffle(choice_copy)
    return choice_copy


def get_random_email() -> str:
    email = (f"{get_random_string()}@"
             f"{get_random_choice(['hotmail.com', 'gmail.com', 'test.com'])}")
    return email


def get_random_sequence(length: int = 10,
                        upper_bound: int = 9, lower_bound: int = 0) -> str:
    LENGHT_DIGITS_LIST = 10
    digits = list(map(str, range(LENGHT_DIGITS_LIST)))
    sequence = [digits[random.randint(lower_bound, upper_bound)]
                for _ in range(length)]
    return ''.join(sequence)


def get_random_phone() -> str:
    return get_random_sequence(10)


def get_random_indexes_without_repeating(length: int = 9,
                                         upper_bound: int = 10,
                                         lower_bound: int = 1) -> list:
    indexes = sample([_ for _ in range(lower_bound, upper_bound)], length)
    return indexes
