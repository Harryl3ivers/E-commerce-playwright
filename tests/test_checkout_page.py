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
    user = User("John","Doe","12345")
    shop_flow.complete_purchase(product,user)
    assert not shop_flow.checkout.has_error()
    assert "Thank you for your order!" in shop_flow.checkout.order_complete()
    

def test_checkout_needs_first_name(shop_flow):
    user = User("","Shaw","12345")
    shop_flow.products.add_product_by_name("Sauce Labs Backpack")
    shop_flow.products.go_to_cart()
    shop_flow.checkout.start_checkout()
    shop_flow.checkout.fill_checkout_info(user)
    shop_flow.checkout.continue_checkout()
    assert shop_flow.checkout.has_error()
    assert "First Name is required" in shop_flow.checkout.get_error_message()

def test_postal_code_required(shop_flow):
    user = User("Noah","Shaw","")
    shop_flow.complete_purchase("Sauce Labs Backpack",user)
    assert  shop_flow.checkout.has_error()
    assert "Error: Postal Code is required" in shop_flow.checkout.get_error_message()

@pytest.mark.parametrize("user",[
   User( "Noah","Shaw","12345"),
    User("Jane","Doe","54321"),
])
def test_checkout_multiple_users(shop_flow,user ):
    shop_flow.complete_purchase("Sauce Labs Backpack",user)
    assert not shop_flow.checkout.has_error()
    assert shop_flow.checkout.order_complete()
    

def test_user_can_recover_from_checkout_error(shop_flow):
    user = User("","Shaw","12345")
    shop_flow.complete_purchase("Sauce Labs Backpack",user)
    assert  shop_flow.checkout.has_error()
    assert "First Name is required" in shop_flow.checkout.get_error_message()

    user.first_name = "Noah"
    shop_flow.checkout.fill_checkout_info(user)
    shop_flow.checkout.continue_checkout()
    assert not shop_flow.checkout.has_error()
    assert "Thank you for your order!" in shop_flow.checkout.order_complete()
     

 