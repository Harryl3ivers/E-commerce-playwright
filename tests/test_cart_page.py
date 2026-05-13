from pages.shopping_cart import ShoppingCart
from pages.products_page import ProductsPage
from conftest import login_page_auto
import pytest
from flows.shop_flow import ShopFlow  
from models.user import User 
from playwright.sync_api import expect
def test_user_can_remove_item_from_cart(login_page_auto):
    products = ProductsPage(login_page_auto)
    cart = ShoppingCart(login_page_auto)

    products.add_product_by_name("Sauce Labs Backpack")
    products.go_to_cart()
    

    cart.remove_first_item()
    assert cart.is_cart_empty()
    

@pytest.mark.parametrize("product", [
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Onesie"
])
def test_that_items_are_in_cart(shop_flow,product):
    shop_flow.products.add_product_by_name(product)
    shop_flow.products.go_to_cart()
    items = shop_flow.products.get_cart_items()
    assert product in items

def test_checkout_empty_cart(shop_flow):
    user = User("Noah","Shaw","12345")
    shop_flow.complete_purchase([],user)
    assert shop_flow.cart.is_cart_empty()

def test_cart_persits_through_navigation(login_page_auto):
    products = ProductsPage(login_page_auto)
    cart = ShoppingCart(login_page_auto)
    products.add_product_by_name("Sauce Labs Backpack")
    products.go_to_cart()
    assert cart.cart_count() == 1
    login_page_auto.go_back()
    products.go_to_cart()
    assert cart.cart_count() == 1

def test_cart_handles_duplicates(login_page_auto):
    products = ProductsPage(login_page_auto)
    products.add_product_by_name(["Sauce Labs Backpack",
        "Sauce Labs Backpack",
        "Sauce Labs Backpack"])
    products.go_to_cart()
    items = products.get_cart_items()
    assert items.count("Sauce Labs Backpack") == 1

def test_product_price_matches_between_inventory_and_cart(login_page_auto):
    products = ProductsPage(login_page_auto)
    cart = ShoppingCart(login_page_auto)
    product_name = "Sauce Labs Backpack"
    inventory_price = float(products.product_price_by_name(product_name).inner_text().replace("$",""))
    products.add_product_by_name(product_name)
    products.go_to_cart()
    cart_price = cart.cart_item_prices()[0]
    assert inventory_price == cart_price

def test_cart_page_persits_after_reload(login_page_auto):
    products = ProductsPage(login_page_auto)
    products.add_first_product_to_cart("Sauce Labs Backpack")
    login_page_auto.reload()
    badge = products.cart_badge()
    expect(badge).to_have_text("1")
    
