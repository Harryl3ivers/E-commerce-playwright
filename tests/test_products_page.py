from products_page import ProductsPage
from login_page import LoginPage
from conftest import *

def test_products_page_add_cart(login_page_auto):
   
    products = ProductsPage(login_page_auto)
    products.add_first_product_to_cart()
    products.go_to_cart()
    assert login_page_auto.locator(".cart_item").count() > 0 ,"user added item to cart"