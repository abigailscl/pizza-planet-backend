import pytest
from app import flask_app

from app.repositories.reports.report import MonthReport, CustomerReport
from app.repositories.models import Ingredient, Order, OrderDetail, db

def test_generate_report_better_month_revenue():
    with flask_app.app_context():
        db.create_all()
        report = MonthReport(Order, db.session)
        order = report.get_better_month_revenue()
        pytest.assume(order is not None)
        pytest.assume(order['month'] is not None)
        pytest.assume(order['sale_amount'] is not None)


def test_generate_report_best_customers():
    NUMBER_BEST_CUSTOMERS = 3
    with flask_app.app_context():
        db.create_all()
        report = CustomerReport(Order, OrderDetail, db.session)
        curtomer = report.get_best_customers()
        pytest.assume(curtomer is not None)
        pytest.assume(len(curtomer) is NUMBER_BEST_CUSTOMERS)


def generate_report_most_requested_ingredient():
    pass