from abc import ABC, abstractmethod

from app.repositories.models import Ingredient, Order, OrderDetail, db
from .report import  Report, MonthReport


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
