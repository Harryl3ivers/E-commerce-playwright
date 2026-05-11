from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.checkout_page import CheckOutPage
from utils.config import STANDARD_USERNAME,PASSWORD
from pages.shopping_cart import ShoppingCart
from flows.shop_flow import ShopFlow   
from models.user import User

def test_full_user_flow(shop_flow):
    user = User("Noah","Shaw","12345")
    shop_flow.complete_purchase("Sauce Labs Backpack",user)
    assert not shop_flow.checkout.error_locator().is_visible()
    assert shop_flow.checkout.complete_header()
  
def test_user_can_complete_multiple_orders(shop_flow,page):
    user = User("Noah","Shaw","12345")
    #first order
    shop_flow.complete_purchase("Sauce Labs Backpack",user)
    assert not shop_flow.checkout.error_locator().is_visible()
    header = shop_flow.checkout.complete_header()
    page.pause()
    assert header.is_visible()
    assert header.inner_text() == "Thank you for your order!"

    shop_flow.checkout.go_back_home()
    
    shop_flow.complete_purchase("Sauce Labs Bike Light", user)
    assert not shop_flow.checkout.error_locator().is_visible()
    header = shop_flow.checkout.complete_header()
    assert header.is_visible()
    assert header.inner_text() == "Thank you for your order!"
     