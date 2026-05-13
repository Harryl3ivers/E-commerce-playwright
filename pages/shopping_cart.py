from pages.base_page import BasePage
class ShoppingCart(BasePage):
    def remove_first_item(self):
        self.click(".cart_item button")
    
    def cart_count(self):
        return self.page.locator(".cart_item").count()
    def is_cart_empty(self)  -> bool:
        return self.cart_count() == 0
    
    def cart_item_names(self):
        return self.page.locator(".inventory_item_name").all_inner_texts()
    
    def cart_item_prices(self):
        prices = self.page.locator(".inventory_item_price").all_inner_texts()
        return[
            float(price.replace("$",""))
            for price in prices
        ]