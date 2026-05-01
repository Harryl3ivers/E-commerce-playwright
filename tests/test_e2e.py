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
    shop_flow.checkout.finish_checkout()
    assert shop_flow.checkout.order_complete()
  
def test_user_can_complete_multiple_orders(shop_flow):
    user = User("Noah","Shaw","12345")
    #first order
    shop_flow.complete_purchase("Sauce Labs Backpack",user)
    assert not shop_flow.checkout.has_error()
    shop_flow.checkout.finish_checkout()

    assert "Thank you for your order!" in shop_flow.checkout.order_complete()

    shop_flow.products.add_product_by_name("Sauce Labs Bike Light")
    shop_flow.products.go_to_cart()

    shop_flow.checkout.start_checkout()
    shop_flow.checkout.fill_checkout_info(user)
    shop_flow.checkout.continue_checkout()
    assert not shop_flow.checkout.has_error()
    shop_flow.checkout.finish_checkout()
    assert "Thank you for your order!" in shop_flow.checkout.order_complete()
     