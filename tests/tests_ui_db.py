from database.queries import get_product_by_price
from pages.products_page import ProductsPage
from flows.shop_flow import ShopFlow
from models.user import User
 
import pytest

def test_product_price_matches_db(login_page_auto):
    products = ProductsPage(login_page_auto)
    product_name = "Sauce Labs Backpack"
    ui_price = products.product_price_by_name(product_name).inner_text()
    ui_price = float(ui_price.replace("$",""))

    database_price = get_product_by_price(product_name)
    database_price = database_price[0]
    assert ui_price == database_price

@pytest.mark.parametrize("product_name",[
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Onesie"
])
def test_multiple_product_prices_matches_db(login_page_auto,product_name):
    products = ProductsPage(login_page_auto)
    ui_price = products.product_price_by_name(product_name).inner_text()
    ui_price = float(ui_price.replace("$",""))

    database_price = get_product_by_price(product_name)
    database_price = database_price[0]
    assert ui_price == database_price

@pytest.mark.parametrize("products_to_buy", [
    ["Sauce Labs Backpack", "Sauce Labs Bike Light"],
    ["Sauce Labs Backpack", "Sauce Labs Onesie"],
])
def test_checkout_subtotal_matches_database(shop_flow, products_to_buy):
    shop_flow.products.add_product_by_name(products_to_buy)
    shop_flow.products.go_to_cart()
    shop_flow.checkout.start_checkout()

    user = User("Noah","Shaw","134GH")
    shop_flow.checkout.fill_checkout_info(user)
    shop_flow.checkout.continue_checkout()

    subtotal_text = shop_flow.checkout.subtotal_label().inner_text()
    ui_subtotal = float(subtotal_text.replace("Item total: $",""))

    total = 0
    for product in products_to_buy:
        price = get_product_by_price(product)
        assert price is not None
        total += price[0]
    assert total == ui_subtotal

  