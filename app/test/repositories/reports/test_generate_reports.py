import pytest
from app import flask_app

from app.repositories.reports.report import MonthReport, CustomerReport, IngredientsReport
from app.repositories.models import Ingredient, Order, OrderDetail, db

def test_get_better_month_revenue():
    with flask_app.app_context():
        db.create_all()
        report = MonthReport(Order, db.session)
        best_month = report.get_better_month_revenue()
        pytest.assume(best_month is not None)
        pytest.assume(best_month['month'] is not None)
        pytest.assume(best_month['sale_amount'] is not None)


def test_get_best_customers():
    NUMBER_BEST_CUSTOMERS = 3
    with flask_app.app_context():
        db.create_all()
        report = CustomerReport(Order, OrderDetail, db.session)
        best_curtomers = report.get_best_customers()
        pytest.assume(best_curtomers is not None)
        pytest.assume(len(best_curtomers) is NUMBER_BEST_CUSTOMERS)


def test_get_best_seller_ingredient():
    with flask_app.app_context():
        db.create_all()
        report = IngredientsReport(Order, OrderDetail, Ingredient, db.session)
        best_ingredient = report.get_best_seller_ingredient()
        print(best_ingredient)
        pytest.assume(best_ingredient['name'] is not None)
        pytest.assume(best_ingredient['count'] > 1)