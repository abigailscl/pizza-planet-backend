import pytest
from ast import Or
from unittest import result
from app import flask_app

from app.repositories.reports.report import MonthReport
from app.repositories.models import Ingredient, Order, OrderDetail, db

def test_generate_report_better_month_revenue():
    with flask_app.app_context():
        db.create_all()
        report = MonthReport(Order, db.session)
        order = report.get_better_month_revenue()
        pytest.assume(order is not None)
        pytest.assume(order['month'] ==  '05')
        pytest.assume(order['sale_amount'] ==  366.97)


def generate_report_best_customers():
    pass


def generate_report_most_requested_ingredient():
    pass