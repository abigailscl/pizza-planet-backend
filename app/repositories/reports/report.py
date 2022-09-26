from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func, desc

from abc import ABC, abstractmethod
from app.repositories.models import db


class Report(ABC):

    @abstractmethod
    def generate_report(self) -> dict:
        pass

class MonthReport(Report):

    def __init__(self, order: db.Model,
                 session: db.session):
        self._order = order
        self._session = session

    def get_better_month_revenue(self):
        month = self._session.query(
            func.strftime("%m", self._order.date).label('month'),
            func.sum(self._order.total_price).label('total')).group_by('month').order_by(desc('total')).first()

        self.orders_not_found(month)

        return {'month_number': month[0], 'total': month[1]}

    def generate_report(self):
        best_month = self.get_better_month_revenue()
        report = best_month
