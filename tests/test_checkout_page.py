from pages.checkout_page import CheckOutPage
from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from flows.shop_flow import ShopFlow
import pytest
from models.user import User

@pytest.mark.parametrize("product",[
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Onesie"
])
def test_user_can_complete_checkout(shop_flow,product):
    user = User("John", "Doe", "12345")
   

    shop_flow.complete_purchase(product,user)

    header = shop_flow.checkout.complete_header()

    assert header.is_visible()
    assert header.inner_text() == "Thank you for your order!"
    

def test_checkout_needs_first_name(shop_flow):
    user = User("","Shaw","12345")
    shop_flow.products.add_product_by_name("Sauce Labs Backpack")
    shop_flow.products.go_to_cart()
    shop_flow.checkout.start_checkout()
    shop_flow.checkout.fill_checkout_info(user)
    shop_flow.checkout.continue_checkout()
    error = shop_flow.checkout.error_locator()
    assert error.is_visible()
    assert "First Name is required" in error.inner_text()
    

def test_postal_code_required(shop_flow):
    user = User("Noah","Shaw","")
    shop_flow.products.add_product_by_name("Sauce Labs Backpack")
    shop_flow.products.go_to_cart()
    shop_flow.checkout.start_checkout()
    shop_flow.checkout.fill_checkout_info(user)
    shop_flow.checkout.continue_checkout()
    error = shop_flow.checkout.error_locator()
    assert error.is_visible()
    assert "Error: Postal Code is required" in error.inner_text()
    

@pytest.mark.parametrize("user",[
   User( "Noah","Shaw","12345"),
    User("Jane","Doe","54321"),
])
def test_checkout_multiple_users(shop_flow,user ):
    shop_flow.complete_purchase("Sauce Labs Backpack",user)
    assert not shop_flow.checkout.error_locator().is_visible()
    assert shop_flow.checkout.complete_header()
    

def test_user_can_recover_from_checkout_error(shop_flow):
    user = User("", "Shaw", "12345")

    # Reach checkout
    shop_flow.products.add_product_by_name("Sauce Labs Backpack")
    shop_flow.products.go_to_cart()
    shop_flow.checkout.start_checkout()

    
    shop_flow.checkout.fill_checkout_info(user)
    shop_flow.checkout.continue_checkout()

    
    error = shop_flow.checkout.error_locator()
    assert error.is_visible()
    assert "First Name is required" in error.inner_text()
    

    
    user.first_name = "Noah"

    # Refill and continue
    shop_flow.checkout.fill_checkout_info(user)
    shop_flow.checkout.continue_checkout()

   
    assert not shop_flow.checkout.error_locator().is_visible()
    shop_flow.checkout.finish_checkout()
    header = shop_flow.checkout.complete_header()
    assert header.is_visible()
    assert header.inner_text() == "Thank you for your order!"
   
     

 