from pages.checkout_page import CheckOutPage
from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from flows.shop_flow import ShopFlow
from database.queries import get_product_by_price
import pytest
from models.user import User
from playwright.sync_api import expect

@pytest.mark.parametrize("product",[
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Onesie"
])
def test_user_can_complete_checkout(shop_flow,product,database_connection):
    user = User("John", "Doe", "12345")
   

    shop_flow.complete_purchase(product,user)

    header = shop_flow.checkout.complete_header()

    expect(header).to_be_visible()
    assert header.inner_text() == "Thank you for your order!"
    price = get_product_by_price(product,database_connection)
    assert price is not None
    

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
    


   
     
def test_checkout_total_is_correct(shop_flow):
    user = User("John","Doe","12345")

    shop_flow.products.add_product_by_name("Sauce Labs Backpack")
    shop_flow.products.go_to_cart()
    shop_flow.checkout.start_checkout()

    shop_flow.checkout.fill_checkout_info(user)
    shop_flow.checkout.continue_checkout()

    subtotal = shop_flow.checkout.subtotal_label()
    tax = shop_flow.checkout.tax_label()
    total = shop_flow.checkout.total_label()

    expect(subtotal).to_have_text("Item total: $29.99")
    expect(tax).to_have_text("Tax: $2.40")
    expect(total).to_have_text("Total: $32.39")

def test_subtotal_is_correct(shop_flow):
    user = User("John", "Doe", "12345")

    shop_flow.products.add_product_by_name("Sauce Labs Backpack")
    shop_flow.products.go_to_cart()

    shop_flow.checkout.start_checkout()
    shop_flow.checkout.fill_checkout_info(user)
    shop_flow.checkout.continue_checkout()

    subtotal = shop_flow.checkout.subtotal_label()

    expect(subtotal).to_have_text("Item total: $29.99")

def test_total_equals_subtotal_plus_tax(shop_flow):
    user = User("John", "Doe", "12345")

    shop_flow.products.add_product_by_name("Sauce Labs Backpack")
    shop_flow.products.go_to_cart()

    shop_flow.checkout.start_checkout()
    shop_flow.checkout.fill_checkout_info(user)
    shop_flow.checkout.continue_checkout() 

    subtotal_text = shop_flow.checkout.subtotal_label().inner_text()
    tax_text = shop_flow.checkout.tax_label().inner_text()
    total_text = shop_flow.checkout.total_label().inner_text()

    subtotal = float(subtotal_text.replace("Item total: $", ""))
    tax = float(tax_text.replace("Tax: $", ""))
    total = float(total_text.replace("Total: $", ""))

    assert round(subtotal + tax,2) == total

def test_multiple_items_total_is_correct(shop_flow):
    user = User("John", "Doe", "12345")
    shop_flow.products.add_product_by_name([
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light"
    ])
    shop_flow.products.go_to_cart()

    shop_flow.checkout.start_checkout()
    shop_flow.checkout.fill_checkout_info(user)
    shop_flow.checkout.continue_checkout()

    subtotal_text = shop_flow.checkout.subtotal_label().inner_text()
    tax_text = shop_flow.checkout.tax_label().inner_text()
    total_text = shop_flow.checkout.total_label().inner_text()

    subtotal = float(subtotal_text.replace("Item total: $", ""))
    tax = float(tax_text.replace("Tax: $", ""))
    total = float(total_text.replace("Total: $", ""))

    assert subtotal == 39.98
    assert round(subtotal + tax,2) == total


