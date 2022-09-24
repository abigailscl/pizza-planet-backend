from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from .template_services import template_service

from ..controllers import IngredientController

ingredient = Blueprint('ingredient', __name__)


@ingredient.route('/', methods=POST)
@template_service
def create_ingredient():
    return IngredientController.create(request.json)


@ingredient.route('/', methods=PUT)
@template_service
def update_ingredient():
    return IngredientController.update(request.json)


@ingredient.route('/id/<_id>', methods=GET)
@template_service
def get_ingredient_by_id(_id: int):
    return IngredientController.get_by_id(_id)


@ingredient.route('/', methods=GET)
@template_service
def get_ingredients():
    return IngredientController.get_all()
