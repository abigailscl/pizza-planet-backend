import pytest
from ast import Or
from unittest import result

from app import flask_app
from collections import Counter
from datetime import datetime

from app.repositories.reports.report_factory import MonthReportFactory
from app.repositories.models import Ingredient, Order, OrderDetail, db

def test_generate_report_better_month_revenue():
    with flask_app.app_context():
        db.create_all()
        dates = []
        report = MonthReportFactory()
        orders = report.get_report().generate_report()
        for order in orders:
            date = datetime.strptime(order['date'], '%Y-%m-%d %H:%M:%S.%f')
            dates.append(date.month)
        counter_dates = Counter(dates)
        result =0
        for order in orders:
            if datetime.strptime(order['date'], '%Y-%m-%d %H:%M:%S.%f').month is not max(counter_dates, key = counter_dates.get):
                continue
            result += order['total_price']
        month_revenue = {'month': max(counter_dates, key = counter_dates.get),  'sale_amount': result}
        pytest.assume(month_revenue == {'month': 6,  'sale_amount': 48.13})


def generate_report_best_customers():
    pass


def generate_report_most_requested_ingredient():
    pass