from app.common.http_methods import GET
from flask import Blueprint, request

from .template_services import template_service

from ..controllers.report import ReportController


report = Blueprint('report', __name__)


@report.route('/month/', methods=GET)
@template_service
def generate_report_better_month_revenue():
    report = ReportController()
    return report.generate_report_better_month_revenue()


@report.route('/customers/', methods=GET)
@template_service
def generate_report_best_customers():
    report = ReportController()
    return report.generate_report_best_customers()


@report.route('/ingredients/', methods=GET)
@template_service
def generate_report_best_seller_ingredient():
    report = ReportController()
    return report.generate_report_best_seller_ingredient()