
import pytest


def test_generate_report_better_month_revenue(client, report_month_uri):
    response = client.get(report_month_uri)
    pytest.assume(response.status.startswith('200'))
    pytest.assume(response.json['month'])
    pytest.assume(response.json['sale_amount'])


def test_generate_report_best_customers(client, report_customers_uri):
    response = client.get(report_customers_uri)
    pytest.assume(response.status.startswith('200'))
    customers = response.jason
    for customer in customers:
        pytest.assume(customer['posicion'])
        pytest.assume(customer['name'])
        pytest.assume(customer['dni'])


def test_generate_report_best_seller_ingredient(client, report_ingredients_uri):
    response = client.get(report_ingredients_uri)
    pytest.assume(response.status.startswith('200'))
    pytest.assume(response['name'])
    pytest.assume(response['count'])
