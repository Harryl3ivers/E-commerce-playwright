from base_page import BasePage

class CheckOutPage(BasePage):
    def start_checkout(self):
        self.click("#checkout")
    
    def fill_checkout_info(self,first_name:str, last_name:str,postal_code:str):
        self.fill("#first-name",first_name)
        self.fill("#last-name",last_name)
        self.fill("#postal-code",postal_code)
    
    def continue_checkout(self):
        self.click("#continue")
    
    def finish_checkout(self):
        self.click("#finish")
    
    def order_complete(self):
        return self.page.locator(".complete-header").inner_text()
    
       