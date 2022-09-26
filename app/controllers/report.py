from sqlalchemy.exc import SQLAlchemyError

from app.repositories.reports.report_factory import (IngredientsReportFactory,
                                                 CustomersReportFactory,
                                                 MonthReportFactory)


class ReportController():

    def generate_report_better_month_revenue(cls):
        try:
            report = MonthReportFactory()
            return report.get_report().generate_report(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
