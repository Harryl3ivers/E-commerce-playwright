from login_page import LoginPage
from products_page import ProductsPage
from checkout_page import CheckOutPage
from utils.config import STANDARD_USERNAME,PASSWORD

def test_full_user_flow(page):
    login = LoginPage(page)
    login.load()
    login.login(STANDARD_USERNAME, PASSWORD)

    products = ProductsPage(page)
    products.add_first_product_to_cart()
    products.go_to_cart()

    checkout = CheckOutPage(page)
    checkout.start_checkout()
    checkout.fill_checkout_info("John","Doe","12345")
    checkout.continue_checkout()
    checkout.finish_checkout()

    assert checkout.order_complete() == "thank you for your order" 