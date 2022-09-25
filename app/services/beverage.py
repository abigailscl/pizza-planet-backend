from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from .template_services import template_service

from ..controllers import BeverageController

beverage = Blueprint('beverage', __name__)


@beverage.route('/', methods=POST)
@template_service
def create_beverage():
    return BeverageController.create(request.json)


@beverage.route('/', methods=PUT)
@template_service
def update_beverage():
    return BeverageController.update(request.json)


@beverage.route('/id/<_id>', methods=GET)
@template_service
def get_beverage_by_id(_id: int):
    return BeverageController.get_by_id(_id)


@beverage.route('/', methods=GET)
@template_service
def get_beverages():
    return BeverageController.get_all()
