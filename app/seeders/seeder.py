from flask_seeder import Seeder, Faker
from flask_seeder.generator import Sequence, Integer

from app.repositories.models import (Beverage, BeverageDetail, Size,
                                     Ingredient, Order, OrderDetail)
from app.test.utils.functions_seeders import (get_random_ingredients,
                                              get_random_beverages,
                                              get_random_sizes)
from app.seeders.generator_fake_data import Datetime, Name, DNI, Phone, Address


UPPER_BOUND_ORDERS = 150
NUMBER_DIGITS = 2

FAKE_SIZES = get_random_sizes(5)
FAKE_BEVERAGES = get_random_beverages(10)
FAKE_INGREDIENTS = get_random_ingredients(10)


class DBSeeder(Seeder):

    def create_order_elements(self, model, data: list):
        faker = Faker(
            cls=model,
            init={
                '_id': Sequence(end=len(data)),
                'name': '',
                'price': 0
            }
        )

        elements = faker.create(len(data))
        for element in elements:
            element.name = data[element._id - 1]['name']
            element.price = data[element.price - 1]['price']
        return elements

    def create_order(self):
        faker_order = Faker(
            cls=Order,
            init={
                '_id': Sequence(end=UPPER_BOUND_ORDERS),
                'client_name': Name(),
                'client_dni': DNI(),
                'client_address': Address(),
                'client_phone': Phone(),
                'date': Datetime(min_year=2022),
                'total_price': 0,
                'size_id': Integer(end=len(FAKE_SIZES)),
            }
        )
        return faker_order

    def create_ingredient(self):
        faker_order_ingredients = Faker(
            cls=OrderDetail,
            init={
                '_id': Sequence(end=UPPER_BOUND_ORDERS),
                'ingredient_price': 0,
                'order_id': Integer(end=UPPER_BOUND_ORDERS),
                'ingredient_id': Integer(end=len(FAKE_INGREDIENTS))
            }
        )
        return faker_order_ingredients

    def create_beverages(self):
        faker_order_beverages = Faker(
            cls=BeverageDetail,
            init={
                '_id': Sequence(end=UPPER_BOUND_ORDERS),
                'beverage_price': 0,
                'order_id': Integer(end=UPPER_BOUND_ORDERS),
                'beverage_id': Integer(end=len(FAKE_BEVERAGES))
                }
            )
        return faker_order_beverages

    def calculate_price_elements(self, order,
                                 order_ingredients, order_beverages):

        total_price_ingredients = (
            sum([ingredient.ingredient_price
                for ingredient in order_ingredients
                if order._id == ingredient.order_id]))
        total_price_beverages = (
                sum([beverage.beverage_price
                    for beverage in order_beverages
                    if order._id == beverage.order_id]))

        return total_price_ingredients, total_price_beverages

    def calculate_order_price(self, orders, clients,
                              order_ingredients, order_beverages):

        for order in orders:
            total_price_ingredients, total_price_beverages = (
                self.calculate_price_elements(
                    order, order_ingredients, order_beverages))
            order.total_price = round(
                FAKE_SIZES[order.size_id - 1]['price'] +
                total_price_ingredients + total_price_beverages, NUMBER_DIGITS)
            if order.client_dni not in clients:
                clients[order.client_dni] = {
                    'name': order.client_name,
                    'address': order.client_address,
                    'phone': order.client_phone
                }
            client = clients[order.client_dni]
            order.client_name = client['name']
            order.client_address = client['address']
            order.client_phone = client['phone']
        return orders

    def set_order_detail(self, order_ingredients, order_beverages):
        for order_ingredient, order_beverage in zip(order_ingredients,
                                                    order_beverages):
            order_ingredient.ingredient_price = (
                FAKE_INGREDIENTS[order_ingredient.ingredient_id - 1]['price'])
            order_beverage.beverage_price = (
                FAKE_INGREDIENTS[order_beverage.beverage_id - 1]['price'])
        return order_ingredients, order_beverages

    def create_orders(self):
        order_ingredients = self.create_ingredient().create(UPPER_BOUND_ORDERS)
        order_beverages = self.create_beverages().create(UPPER_BOUND_ORDERS)
        new_order_ingredients, new_order_beverages = self.set_order_detail(
            order_ingredients, order_beverages)

        clients = dict()
        orders = self.create_order().create(UPPER_BOUND_ORDERS)
        new_orders = self.calculate_order_price(
            orders, clients, new_order_ingredients, new_order_beverages)
        return new_orders, order_ingredients, order_beverages

    def run(self):
        sizes = self.create_order_elements(Size, FAKE_SIZES)
        ingredients = self.create_order_elements(Ingredient, FAKE_INGREDIENTS)
        beverages = self.create_order_elements(Beverage, FAKE_BEVERAGES)
        orders, order_ingredients, order_beverages = self.create_orders()

        self.db.session.add_all(sizes)
        self.db.session.add_all(ingredients)
        self.db.session.add_all(beverages)
        self.db.session.add_all(orders)
        self.db.session.add_all(order_ingredients)
        self.db.session.add_all(order_beverages)
        self.db.session.commit()
