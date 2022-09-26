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
    
    def orders_not_found(self, model):
        if not model:
            raise SQLAlchemyError("Sorry,there aren't orders")
    
    def get_better_month_revenue(self):
        month = self._session.query(
            func.strftime("%m", self._order.date).label('month'),
            func.sum(self._order.total_price).label('total')).group_by('month').order_by(desc('total')).first()
        self.orders_not_found(month)
        return {'month': month[0], 'sale_amount': round(month[1],2)}

    def generate_report(self):
        best_month = self.get_better_month_revenue()
        report = best_month


class CustomerReport(Report):

    def __init__(self, order: db.Model,
                 order_detail: db.Model,
                 session: db.session):
        self._order = order
        self._order_detail = order_detail
        self._session = session

    def orders_not_found(self, model):
        if not model:
            raise SQLAlchemyError("Sorry,there aren't orders")

    def get_best_customers(self):
        customers = self._session.query(
            self._order.client_name, self._order.client_dni,
            func.count(self._order.client_dni).label('count')
        ).group_by(self._order.client_dni).order_by(desc('count')).limit(3).all()

        self.orders_not_found(customers)

        return [{'posicion': posicion + 1, 'name': customer.client_name, 'dni': customer.client_dni}
                for posicion, customer in enumerate(customers)]

    def generate_report(self):
        best_customers = self.get_best_customers()

        report = best_customers