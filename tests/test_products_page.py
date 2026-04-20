from products_page import ProductsPage
from login_page import LoginPage

def test_products_page_add_cart(page):
    login = LoginPage(page)
    login.load()
    login.login("standard_user","secret_sauce")
    products = ProductsPage(page)
    products.add_first_product_to_cart()
    products.go_to_cart()
    assert page.locator(".cart_item").count() > 0 ,"user added item to cart"