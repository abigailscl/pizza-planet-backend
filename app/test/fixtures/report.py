import pytest


@pytest.fixture
def report_month_uri():
    return '/report/month/'


@pytest.fixture
def report_customers_uri():
    return '/report/customers/'


@pytest.fixture
def report_ingredients_uri():
    return '/report/ingredients/'