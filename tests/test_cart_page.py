from shopping_cart import ShoppingCart
from products_page import ProductsPage
from conftest import login_page_auto
import pytest


def test_user_can_remove_item_from_cart(login_page_auto):
    products_page = ProductsPage(login_page_auto)
    products_page.add_first_product_to_cart()
    products_page.go_to_cart()

    cart_page = ShoppingCart(login_page_auto)
    assert cart_page.cart_count() == 1

    cart_page.remove_first_item()
    assert cart_page.cart_empty()