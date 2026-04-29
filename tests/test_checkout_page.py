from checkout_page import CheckOutPage
from products_page import ProductsPage
from login_page import LoginPage
from  conftest import login_page_auto
from conftest import shop_flow
from shop_flow import ShopFlow
import pytest
from user import User

@pytest.mark.parametrize("product",[
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Onesie"
])
def test_user_can_complete_checkout(shop_flow,product):
    user = User("John","Doe","12345")
    shop_flow.complete_purchase(product,user)
    assert "Thank you for your order!" in shop_flow.checkout.order_complete()
    

def test_checkout_needs_first_name(shop_flow):
    user = User("","Shaw","12345")
    shop_flow.complete_purchase("Sauce Labs Backpack",user)

    assert "First Name is required" in shop_flow.checkout.get_error_message()

def test_postal_code_required(shop_flow):
    user = User("Noah","Shaw","")
    shop_flow.complete_purchase("Sauce Labs Backpack",user)
    assert "Error: Postal Code is required" in shop_flow.checkout.get_error_message()

@pytest.mark.parametrize("user",[
   User( "Noah","Shaw","12345"),
    User("Jane","Doe","54321"),
])
def test_checkout_multiple_users(shop_flow,user ):
    shop_flow.complete_purchase("Sauce Labs Backpack",user)
    assert shop_flow.checkout.order_complete()
    
    
     

 