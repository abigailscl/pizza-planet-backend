import random

from flask_seeder.generator import Generator
from datetime import datetime, timedelta

from app.test.utils.functions_seeders import get_random_addresses, get_random_list_dni, get_random_names, get_random_phones

UPPER_BOUND_ORDERS = 150
CLIENTS_AMOUNT = 150

def read_resource(path):
    """ Read resource text file
    Reads resource text file and returns content as a list.
    Arguments:
        path: The resource path relative to the data root directory
    Returns:
        A list with the file contents.
    """
    lines = []
    with open(path) as source:
        lines = source.read().splitlines()

    return lines


class Datetime(Generator):

    def __init__(self, min_year=2021, max_year=datetime.now(), **kwargs):
        super(**kwargs).__init__()
        self._min_year = min_year
        self._max_year = max_year

    def generate(self):
        DAYS_YEAR = 365
        start = datetime(self._min_year, 1, 1, 00, 00, 00)
        end = self._max_year
        if not isinstance(self._max_year, datetime):
            years = self._max_year - self._min_year + 1
            end = start + timedelta(days=DAYS_YEAR * years)
        return start + (end - start) * random.random()


class Name(Generator):
    """ Random Name generator """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._lines = None

    def generate(self):
        """ Generate a random name
        Returns:
            A random name in string format
        """
        if self._lines is None:
            self._lines = get_random_names('it_IT', UPPER_BOUND_ORDERS)

        result = self.rnd.choice(self._lines)

        return result


class DNI(Generator):
    """ Random DNI generator """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._lines = None

    def generate(self):
        """ Generate a random DNI
        Returns:
            A random DNI in string format
        """
        if self._lines is None:
            self._lines = get_random_list_dni(UPPER_BOUND_ORDERS)

        result = self.rnd.choice(self._lines)

        return result


class Address(Generator):
    """ Random Address generator """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._lines = None

    def generate(self):
        """ Generate a random DNI
        Returns:
            A random Address in string format
        """
        if self._lines is None:
            self._lines = get_random_addresses(UPPER_BOUND_ORDERS)

        result = self.rnd.choice(self._lines)

        return result


class Phone(Generator):
    """ Random Phone generator """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._lines = None

    def generate(self):
        """ Generate a random Phone
        Returns:
            A random Phones in string format
        """
        if self._lines is None:
            self._lines = get_random_phones(UPPER_BOUND_ORDERS)

        result = self.rnd.choice(self._lines)

        return result