
class ShopFlow():
    def __init__(self,products,cart,checkout):
        self.products = products
        self.cart = cart
        self.checkout = checkout
    def complete_purchase(self,product,first,last,postal):
        self.products.add_product_by_name(product)
        self.products.go_to_cart()

        self.checkout.start_checkout()
        self.checkout.fill_checkout_info(first,last,postal)
        self.checkout.continue_checkout()
        self.checkout.finish_checkout()