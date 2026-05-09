from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.checkout_page import CheckOutPage
from utils.config import STANDARD_USERNAME,PASSWORD
from pages.shopping_cart import ShoppingCart
from flows.shop_flow import ShopFlow   
from models.user import User

def test_full_user_flow(shop_flow):
    user = User("Noah","Shaw","12345")
    shop_flow.complete_purchase(["Sauce Labs Backpack"],user)
    assert not shop_flow.checkout.has_error()
    
    assert shop_flow.checkout.order_complete()
  
def test_user_can_complete_multiple_orders(shop_flow):
    user = User("Noah","Shaw","12345")
    #first order
    shop_flow.complete_purchase("Sauce Labs Backpack",user)
    assert not shop_flow.checkout.has_error()
    assert shop_flow.checkout.order_complete()

    assert "Thank you for your order!" in shop_flow.checkout.order_complete()
    shop_flow.checkout.go_back_home()
    
    shop_flow.complete_purchase("Sauce Labs Bike Light", user)
    assert not shop_flow.checkout.has_error()
    assert "Thank you for your order!" in shop_flow.checkout.order_complete()
     