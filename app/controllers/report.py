from sqlalchemy.exc import SQLAlchemyError

from ..repositories.managers import BaseManager
from app.repositories.reports.report import *
from app.repositories.models import Ingredient, Order, OrderDetail, db


class ReportController():

    @classmethod
    def generate_report_better_month_revenue(cls):
        try:
            report = MonthReport(Order, db.session)
            print(report.generate_report())
            return report.generate_report(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            print('error')
            return None, str(ex)

    @classmethod
    def generate_report_best_customers(cls):
        try:
            report = CustomerReport(Order, OrderDetail, db.session)
            return report.generate_report(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    @classmethod
    def generate_report_best_seller_ingredient(cls):
        try:
            report = IngredientsReport(Order, OrderDetail, Ingredient, db.session)
            return report.generate_report(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
