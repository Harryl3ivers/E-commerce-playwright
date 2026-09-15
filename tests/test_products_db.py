import pytest
from database.queries import get_product_by_name,get_product_by_price,get_order_by_id,get_order_product


def test_product_exist_in_db(database_connection):
    product = get_product_by_name("Sauce Labs Backpack",database_connection)
    assert product is not None
    assert product[1] == "Sauce Labs Backpack"

def test_product_price_in_database(database_connection):
    product = get_product_by_price("Sauce Labs Backpack",database_connection)

    assert product[0] == 29.99

@pytest.mark.parametrize("product_name,expected_price",[
    ("Sauce Labs Backpack",29.99),("Sauce Labs Bike Light",9.99)
])
def test_multiple_product_prices_in_database(product_name,expected_price,database_connection):
    price = get_product_by_price(product_name,database_connection)
    assert price[0] == expected_price

def test_order_exists_in_database(database_connection):
    order = get_order_by_id(1,database_connection)
    assert order is not None
    assert order[0] == 1
    assert order[2] == 29.99
    assert order[3] == "completed"

def test_order_contains_correct_product(database_connection):
    order_product = get_order_product(1,database_connection)
    assert order_product is not None
    assert order_product[1] == "Sauce Labs Backpack"
    assert order_product[2] == 1
    assert order_product[3] == 29.99

def test_order_does_not_exist(database_connection):
    product = get_product_by_name("Product that does not exist",database_connection)
    assert product is None