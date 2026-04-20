from checkout_page import CheckOutPage
from products_page import ProductsPage
from login_page import LoginPage
from utils.config import STANDARD_USERNAME,PASSWORD
from  conftest import *

def test_user_can_complete_checkout(login_page_auto):
    
    
    products_page = ProductsPage(login_page_auto)
    products_page.add_first_product_to_cart()
    products_page.go_to_cart()

    checkout = CheckOutPage(login_page_auto)
    checkout.start_checkout()
    checkout.fill_checkout_info("Harry","Leivers","12345")
    checkout.continue_checkout()
    checkout.finish_checkout()

    assert "thank you for your order!" in checkout.order_complete().lower()

def test_checkout_needs_first_name(login_page_auto):
    

    products_page = ProductsPage(login_page_auto)
    products_page.add_first_product_to_cart()
    products_page.go_to_cart()

    checkout_page = CheckOutPage(login_page_auto)
    checkout_page.start_checkout()
    checkout_page.fill_checkout_info("", "Doe", "12345")
    checkout_page.continue_checkout()

    assert "First Name is required" in checkout_page.get_error_message()

def test_postal_code_required(login_page_auto):
    products_page = ProductsPage(login_page_auto)
    products_page.add_first_product_to_cart()
    products_page.go_to_cart()

    checkout_page = CheckOutPage(login_page_auto)
    checkout_page.start_checkout()
    checkout_page.fill_checkout_info("John", "Doe", "")
    checkout_page.continue_checkout()
    assert "Postal Code is required" in checkout_page.get_error_message()
     