import pytest

from app.controllers.report import ReportController


def tes_get_report_better_month_revenue():
    report, error = ReportController.generate_report_better_month_revenue()
    pytest.assume(error is None)
    pytest.assume(report['customers'] is not None)
    pytest.assume(report['ingredient'] is not None)
    pytest.assume(report['month'] is not None)


def tes_get_report_best_customers():
    NUMBER_BEST_CUSTOMERS = 3
    report, error = ReportController.generate_report_best_customers()
    pytest.assume(error is None)
    pytest.assume(report is not None)
    pytest.assume(len(report) is NUMBER_BEST_CUSTOMERS)


def test_generate_report_best_seller_ingredient():
    report, error = ReportController.generate_report_best_seller_ingredient()
    pytest.assume(report['name'] is not None)
    pytest.assume(report['count'] > 1)