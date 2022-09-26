import pytest
from app import flask_app

from app.controllers.report import *


def test_generate_report_better_month_revenue():
    with flask_app.app_context():
        db.create_all()
        report = ReportController()
        best_month = report.generate_report_better_month_revenue()
        pytest.assume(best_month is not None)
        pytest.assume(best_month['month'] is not None)
        pytest.assume(best_month['sale_amount'] is not None)


def test_generate_report_best_customers():
    NUMBER_BEST_CUSTOMERS = 3
    with flask_app.app_context():
        db.create_all()
        report = ReportController()
        best_curtomers = report.generate_report_best_customers()
        pytest.assume(best_curtomers is not None)
        pytest.assume(len(best_curtomers) is NUMBER_BEST_CUSTOMERS)


def test_generate_report_best_seller_ingredient():
    with flask_app.app_context():
        db.create_all()
        report = ReportController()
        best_ingredient = report.generate_report_best_seller_ingredient()
        pytest.assume(best_ingredient['name'] is not None)
        pytest.assume(best_ingredient['count'] > 1)