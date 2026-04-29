from shopping_cart import ShoppingCart
from products_page import ProductsPage
from conftest import login_page_auto
import pytest
from shop_flow import ShopFlow  
from user import User 

def test_user_can_remove_item_from_cart(login_page_auto):
    products = ProductsPage(login_page_auto)
    cart = ShoppingCart(login_page_auto)

    products.add_product_by_name("Sauce Labs Backpack")
    products.go_to_cart()

    cart.remove_first_item()
    assert cart.is_cart_empty()
    

def test_that_items_are_in_cart(shop_flow,product):
    shop_flow.products.add_product_by_name(product)
    shop_flow.products.go_to_cart()
    items = shop_flow.products.get_cart_items()
    assert product in items

def test_checkout_empty_cart(shop_flow):
    user = User("Noah","Shaw","12345")
    shop_flow.complete_purchase([],user)
    assert shop_flow.cart.is_cart_empty()