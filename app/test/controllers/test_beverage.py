import pytest
from app.controllers import BeverageController
from app.test.utils.functions import get_random_indexes_without_repeating


def test_create(app, beverage: dict):
    created_beverage, error = BeverageController.create(beverage)
    pytest.assume(error is None)
    for param, value in beverage.items():
        pytest.assume(param in created_beverage)
        pytest.assume(value == created_beverage[param])
        pytest.assume(created_beverage['_id'])


def test_update(app, beverage: dict):
    created_beverage, _ = BeverageController.create(beverage)
    updated_fields = {
        'name': 'updated',
        'price': 10
    }
    updated_beverage, error = BeverageController.update({
        '_id': created_beverage['_id'],
        **updated_fields
    })
    pytest.assume(error is None)
    beverage_from_database, error = BeverageController.get_by_id(
        created_beverage['_id'])
    pytest.assume(error is None)
    for param, value in updated_fields.items():
        pytest.assume(updated_beverage[param] == value)
        pytest.assume(beverage_from_database[param] == value)


def test_get_by_id(app, beverage: dict):
    created_beverage, _ = BeverageController.create(beverage)
    beverage_from_database, error = BeverageController.get_by_id(
        created_beverage['_id'])
    pytest.assume(error is None)
    for param, value in created_beverage.items():
        pytest.assume(beverage_from_database[param] == value)


def test_get_all(app, beverages: list):
    created_beverages = []
    for beverage in beverages:
        created_beverage, _ = BeverageController.create(beverage)
        created_beverages.append(created_beverage)

    beverages_from_database, error = BeverageController.get_all()
    searchable_beverages = {db_beverage['_id']: db_beverage
                            for db_beverage in beverages_from_database}
    pytest.assume(error is None)
    for created_beverage in created_beverages:
        current_id = created_beverage['_id']
        assert current_id in searchable_beverages
        for param, value in created_beverage.items():
            pytest.assume(searchable_beverages[current_id][param] == value)


def test_get_by_id_list(app, beverages: dict):
    created_beverages = []
    beverage_ids = []
    ORDERED_BEVERAGES = 3
    for beverage in beverages:
        created_beverage, _ = BeverageController.create(beverage)
        created_beverages.append(created_beverage)
    beverage_ids = get_random_indexes_without_repeating(
        ORDERED_BEVERAGES, len(created_beverages))

    beverages_from_database, error = BeverageController.get_by_id_list(
        beverage_ids)
    searchable_beverages = {db_beverage.__dict__['_id']: db_beverage.__dict__
                            for db_beverage in beverages_from_database}
    pytest.assume(error is None)
    for created_beverage in created_beverages:
        current_id = created_beverage['_id']
        for param, value in created_beverage.items():
            if(current_id in searchable_beverages):
                pytest.assume(searchable_beverages[current_id][param] == value)
