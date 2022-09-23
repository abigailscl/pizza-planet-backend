import pytest
from app.controllers import (IngredientController, OrderController,
                             BeverageController, SizeController)
from app.controllers.base import BaseController


def __order(ingredients: list, beverages: list, size: dict, client_data: dict):
    ingredients = [ingredient.get('_id') for ingredient in ingredients]
    beverages = [beverage.get('_id') for beverage in beverages]
    size_id = size.get('_id')
    return {
        **client_data,
        'ingredients': ingredients,
        'beverages': beverages,
        'size_id': size_id
    }


def __create_items(items: list, controller: BaseController):
    created_items = []
    for element_of_order in items:
        created_item, _ = controller.create(element_of_order)
        created_items.append(created_item)
    return created_items


def __create_sizes_ingredients_beverages(ingredients: list,
                                         beverages: list, sizes: list):
    created_ingredients = __create_items(ingredients, IngredientController)
    created_beverages = __create_items(beverages, BeverageController)
    created_sizes = __create_items(sizes, SizeController)
    return (created_sizes if len(created_sizes) > 1 else created_sizes.pop(),
            created_ingredients, created_beverages)


def test_create(app, ingredients, beverages, size, client_data):
    created_size, created_ingredients, created_beverages = (
        __create_sizes_ingredients_beverages(ingredients, beverages, [size]))
    order = __order(created_ingredients,
                    created_beverages, created_size, client_data)
    created_order, error = OrderController.create(order)
    size_id = order.pop('size_id', None)
    ingredient_ids = order.pop('ingredients', [])
    beverage_ids = order.pop('beverages', [])
    pytest.assume(error is None)
    for param, value in order.items():
        pytest.assume(param in created_order)
        pytest.assume(value == created_order[param])
        pytest.assume(created_order['_id'])
        pytest.assume(size_id == created_order['size']['_id'])

        ingredients_in_detail = set(item['ingredient']['_id']
                                    for item in created_order['detail'])
        beverages_in_detail = set(item['beverage']['_id']
                                  for item in created_order['beverage_detail'])
        pytest.assume(not ingredients_in_detail.difference(ingredient_ids))
        pytest.assume(not beverages_in_detail.difference(beverage_ids))


def test_calculate_order_price(app, ingredients, beverages, size, client_data):
    NUMBER_DIGITS = 2
    created_size, created_ingredients, created_beverages = (
        __create_sizes_ingredients_beverages(ingredients, beverages, [size]))
    order = __order(created_ingredients,
                    created_beverages, created_size, client_data)
    created_order, _ = OrderController.create(order)
    pytest.assume(created_order['total_price'] == round(created_size['price'] +
                  sum(ingredient['price']
                      for ingredient in created_ingredients) +
                  sum(beverage['price']
                      for beverage in created_beverages), NUMBER_DIGITS))
