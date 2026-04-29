from user import User
from checkout_page import CheckOutPage

class ShopFlow():
    def __init__(self,products,cart,checkout):
        self.products = products
        self.cart = cart
        self.checkout = checkout
    def complete_purchase(self, products: list[str], user: User):
        self.products.add_product_by_name(products)
        self.products.go_to_cart()

        self.checkout.start_checkout()
        self.checkout.fill_checkout_info(user)
        self.checkout.continue_checkout()
        if self.checkout.has_error():
            return
        self.checkout.finish_checkout()