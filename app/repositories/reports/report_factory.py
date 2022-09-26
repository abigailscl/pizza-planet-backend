from abc import ABC, abstractmethod

from app.repositories.models import Ingredient, Order, OrderDetail, db
from .report import Report, MonthReport, CustomerReport, IngredientsReport


class ReportFactory(ABC):
    @abstractmethod
    def get_report(self) -> Report:
        pass


class MonthReportFactory(ReportFactory):
    def __init__(self):
        self._order = Order
        self._session = db.session

    def get_report(self) -> Report:
        return MonthReport(self._order,
                           self._session
                           )


class CustomersReportFactory(ReportFactory):
    def __init__(self):
        self._order = Order
        self._order_detail = OrderDetail
        self._session = db.session

    def get_report(self) -> Report:
        return CustomerReport(self._order,
                              self._order_detail,
                              self._session)


class IngredientsReportFactory(ReportFactory):
    def __init__(self):
        self._order = Order
        self._order_detail = OrderDetail
        self._session = db.session
        self._ingredient = Ingredient

    def get_report(self) -> Report:
        return IngredientsReport(self._order,
                                 self._order_detail,
                                 self._ingredient,
                                 self._session)
