from base_page import BasePage

class ProductsPage(BasePage):
    def add_first_product_to_cart(self):
        self.click(".inventory_item button")
        print("CLICKED ITEM!!!!")
    
    def go_to_cart(self):
        self.click(".shopping_cart_link")
    