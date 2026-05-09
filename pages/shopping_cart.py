from pages.base_page import BasePage
class ShoppingCart(BasePage):
    def remove_first_item(self):
        self.click(".cart_item button")
    
    def cart_count(self):
        return self.page.locator(".cart_item").count()
    def is_cart_empty(self)  -> bool:
        return self.cart_count() == 0