from ast import Or
from unittest import result
import pytest
from collections import Counter
from datetime import datetime

ORDERS = [
    {
        "_id": 1,
        "beverage_detail": [
            {
                "beverage": {
                    "_id": 4,
                    "name": "Sprite",
                    "price": 2.8
                },
                "beverage_price": 2.25
            }
        ],
        "client_address": "151 Brittany Branch\nNew Jessica, SC 16737",
        "client_dni": "355-36-9784",
        "client_name": "Eugenia Speri",
        "client_phone": "396.029.8688x51960",
        "date": "2022-06-26 10:35:27.669339",
        "detail": [
            {
                "ingredient": {
                    "_id": 10,
                    "name": "olives",
                    "price": 1.1
                },
                "ingredient_price": 1.1
            },
            {
                "ingredient": {
                    "_id": 9,
                    "name": "Onion",
                    "price": 1.1
                },
                "ingredient_price": 1.1
            },
            {
                "ingredient": {
                    "_id": 13,
                    "name": "Mushroom",
                    "price": 1.1
                },
                "ingredient_price": 1.1
            }
        ],
        "size": {
            "_id": 3,
            "name": "Medium",
            "price": 23.99
        },
        "total_price": 14.54
    },
    {
        "_id": 2,
        "beverage_detail": [
            {
                "beverage": {
                    "_id": 4,
                    "name": "Sprite",
                    "price": 2.8
                },
                "beverage_price": 2.25
            },
            {
                "beverage": {
                    "_id": 1,
                    "name": "Pepsi",
                    "price": 2.8
                },
                "beverage_price": 2.25
            }
        ],
        "client_address": "70243 Gregory Passage\nLeborough, RI 75214",
        "client_dni": "413-38-7533",
        "client_name": "Gloria Mercati-Giradello",
        "client_phone": "(235)532-5543",
        "date": "2022-05-09 18:35:15.271305",
        "detail": [],
        "size": {
            "_id": 2,
            "name": "Personal",
            "price": 23.99
        },
        "total_price": 11.49
    },
    {
        "_id": 3,
        "beverage_detail": [
            {
                "beverage": {
                    "_id": 4,
                    "name": "Sprite",
                    "price": 2.8
                },
                "beverage_price": 2.25
            },
            {
                "beverage": {
                    "_id": 2,
                    "name": "Fioravanti",
                    "price": 2.8
                },
                "beverage_price": 2.55
            }
        ],
        "client_address": "PSC 6559, Box 8104\nAPO AA 33055",
        "client_dni": "492-79-8329",
        "client_name": "Salvatore Ficino-Mondaini",
        "client_phone": "+1-537-799-3496x68714",
        "date": "2022-06-30 00:37:47.110615",
        "detail": [
            {
                "ingredient": {
                    "_id": 2,
                    "name": "Cheese",
                    "price": 1.1
                },
                "ingredient_price": 2.55
            },
            {
                "ingredient": {
                    "_id": 7,
                    "name": "Ham",
                    "price": 1.1
                },
                "ingredient_price": 2.25
            }
        ],
        "size": {
            "_id": 5,
            "name": "Big",
            "price": 23.99
        },
        "total_price": 33.59
    },
    {
        "_id": 4,
        "beverage_detail": [
            {
                "beverage": {
                    "_id": 1,
                    "name": "Pepsi",
                    "price": 2.8
                },
                "beverage_price": 2.25
            }
        ],
        "client_address": "57317 Zimmerman Ferry Suite 927\nWest Emily, ME 65870",
        "client_dni": "464-96-9594",
        "client_name": "Viridiana Comboni-Marenzio",
        "client_phone": "+1-413-013-7123x21914",
        "date": "2022-02-25 02:37:04.916804",
        "detail": [],
        "size": {
            "_id": 2,
            "name": "Personal",
            "price": 23.99
        },
        "total_price": 9.24
    },
    {
        "_id": 5,
        "beverage_detail": [
            {
                "beverage": {
                    "_id": 1,
                    "name": "Pepsi",
                    "price": 2.8
                },
                "beverage_price": 2.25
            }
        ],
        "client_address": "2122 Barnes Spring\nJasonhaven, KY 56263",
        "client_dni": "684-32-1484",
        "client_name": "Gastone Bernetti",
        "client_phone": "(412)895-3501x6001",
        "date": "2022-07-23 19:49:27.709739",
        "detail": [],
        "size": {
            "_id": 5,
            "name": "Big",
            "price": 23.99
        },
        "total_price": 26.24
    }
]


def test_generate_report_better_month_revenue():
    total_prices = []
    dates = []
    for order in ORDERS:
        date = datetime.strptime(order['date'], '%Y-%m-%d %H:%M:%S.%f')
        dates.append(date.month)
    counter_dates = Counter(dates)
    result =0
    for order in ORDERS:
        if datetime.strptime(order['date'], '%Y-%m-%d %H:%M:%S.%f').month is not max(counter_dates, key = counter_dates.get):
            continue
        result += order['total_price']
    month_revenue = {'month': max(counter_dates, key = counter_dates.get),  'sale_amount': result}
    pytest.assume(month_revenue == {'month': 6,  'sale_amount': 48.13})


def generate_report_best_customers():
    pass


def generate_report_most_requested_ingredient():
    pass