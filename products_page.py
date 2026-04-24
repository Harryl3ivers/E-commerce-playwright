from base_page import BasePage

class ProductsPage(BasePage):
    def get_cart_items(self):
        return self.page.locator(".cart_item .inventory_item_name").all_inner_texts()

    def add_first_product_to_cart(self):
        self.page.locator("[data-test^='add-to-cart']").first.click()
    
    def add_product_by_name(self, product_names: list[str] | str) -> list[str]:
        if isinstance(product_names, str):
            product_names = [product_names]

        added_items = []

        for name in product_names:
            self.page.locator(".inventory_item") \
            .filter(has_text=name) \
            .get_by_role("button", name="Add to cart") \
            .click()
            added_items.append(name)

        return added_items
        
    
    def go_to_cart(self):
        self.click(".shopping_cart_link")
    