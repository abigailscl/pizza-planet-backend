import pytest

from app.controllers.report import ReportController


def tes_get_report_better_month_revenue():
    report, error = ReportController.generate_report_better_month_revenue()
    pytest.assume(error is None)
    pytest.assume(report['customers'] is not None)
    pytest.assume(report['ingredient'] is not None)
    pytest.assume(report['month'] is not None)


def tes_get_report_best_customers():
    pass


def test_generate_report_best_seller_ingredient():
    pass