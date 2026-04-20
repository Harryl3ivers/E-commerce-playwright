from checkout_page import CheckOutPage
from products_page import ProductsPage
from login_page import LoginPage
from utils.config import STANDARD_USERNAME,PASSWORD

def test_user_can_complete_checkout(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login(STANDARD_USERNAME,PASSWORD)
    
    products_page = ProductsPage(page)
    products_page.add_first_product_to_cart()
    products_page.go_to_cart()

    checkout = CheckOutPage(page)
    checkout.start_checkout()
    checkout.fill_checkout_info("Harry","Leivers","12345")
    checkout.continue_checkout()
    checkout.finish_checkout()

    assert "thank you for your order!" in checkout.order_complete().lower()