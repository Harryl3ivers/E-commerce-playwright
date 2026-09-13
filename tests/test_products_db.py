import pytest
from database.queries import get_product_by_name,get_product_by_price,get_order_by_id


def test_product_exist_in_db():
    product = get_product_by_name("Sauce Labs Backpack")
    assert product is not None
    assert product[1] == "Sauce Labs Backpack"

def test_product_price_in_database():
    product = get_product_by_price("Sauce Labs Backpack")

    assert product[0] == 29.99

@pytest.mark.parametrize("product_name,expected_price",[
    ("Sauce Labs Backpack",29.99),("Sauce Labs Bike Light",9.99)
])
def test_multiple_product_prices_in_database(product_name,expected_price):
    price = get_product_by_price(product_name)
    assert price[0] == expected_price

def test_order_exists_in_database( ):
    order = get_order_by_id(1)
    assert order is not None
    assert order[0] == 1
    assert order[0] == 29.99
    assert order[0] == "completed"