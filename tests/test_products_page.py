from pages.products_page import ProductsPage
from conftest import login_page_auto
from pages.shopping_cart import ShoppingCart
import pytest

def test_products_page_add_cart(login_page_auto):
   
    products = ProductsPage(login_page_auto)
    products.add_first_product_to_cart()
    products.go_to_cart()
    assert login_page_auto.locator(".cart_item").count() > 0 ,"user added item to cart"

def test_add_product_name(login_page_auto):
    products = ProductsPage( login_page_auto)
    products.add_product_by_name("Sauce Labs Backpack")
    products.go_to_cart()
    item = login_page_auto.locator(".inventory_item_name")
    assert item.is_visible()
    assert item.inner_text() == "Sauce Labs Backpack"

@pytest.mark.parametrize("products",[
    ["Sauce Labs Backpack"],
    ["Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt"],
    ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Onesie"]
])
def test_add_multiple_products(login_page_auto,products):
    product = ProductsPage(login_page_auto)
    added = product.add_product_by_name(products)
    product.go_to_cart()
    cart_items = product.get_cart_items()
    assert set(cart_items) == set(products) 
    assert len(cart_items) == len(products) 
    assert added == products