from abc import ABC, abstractmethod

from app.repositories.models import Ingredient, Order, OrderDetail, db
from .report import Report, CustomersReport


class ReportFactory(ABC):
    @abstractmethod
    def get_report(self) -> Report:
        pass

class CustomersReport(ReportFactory):
    def __init__(self):
        self._order = Order
        self._order_detail = OrderDetail
        self._session = db.session
        self._ingredient = Ingredient

    def get_report(self) -> Report:
        return CustomersReport(self._order,
                           self._order_detail,
                           self._session
                           )
