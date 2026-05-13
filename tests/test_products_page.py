from pages.products_page import ProductsPage
from conftest import login_page_auto
from pages.shopping_cart import ShoppingCart
import pytest
from playwright.sync_api import expect

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

def test_products_sort_low_to_high(login_page_auto):
    product = ProductsPage(login_page_auto)
    product.sort_products("lohi")
    prices = product.product_prices()
    assert prices == sorted(prices)

def test_products_sort_high_to_low(login_page_auto):
    product = ProductsPage(login_page_auto)
    product.sort_products("hilo")
    prices = product.product_prices()
    assert prices == sorted(prices,reverse=True)

def test_products_sort_name_a_to_z(login_page_auto):
    product = ProductsPage(login_page_auto)
    product.sort_products("az")
    names = product.product_names()
    assert names == sorted(names)

def test_products_sort_name_z_to_a(login_page_auto):
    product = ProductsPage(login_page_auto)
    product.sort_products("za")
    names = product.product_names()
    assert names == sorted(names,reverse=True)


def test_cart_badge_update_when_adding_items(login_page_auto):
    products = ProductsPage(login_page_auto)
    products.add_product_by_name("Sauce Labs Backpack")
    badge = products.cart_badge()
    expect(badge).to_have_text("1")

def test_cart_badge_increments(login_page_auto):
    products = ProductsPage(login_page_auto)

    products.add_product_by_name([
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light"
    ])

    badge = products.cart_badge()
    expect(badge).to_have_text("2")