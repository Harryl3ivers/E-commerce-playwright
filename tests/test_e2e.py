from login_page import LoginPage
from products_page import ProductsPage

def test_full_user_flow(page):
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(page)
    products.add_first_product_to_cart()
    products.go_to_cart()

    page.click("#checkout")
    page.fill("#first-name", "John")
    page.fill("#last-name", "Doe")
    page.fill("#postal-code", "12345")
    page.click("#continue")
    page.click("#finish")

    assert "thank you for your order" in page.content().lower()