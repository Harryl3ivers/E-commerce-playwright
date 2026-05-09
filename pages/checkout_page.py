from pages.base_page import BasePage
from models.user import User
from playwright.sync_api import expect

class CheckOutPage(BasePage):
    CHECKOUT_BUTTON = "#checkout"
    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    POSTAL_CODE = "#postal-code"
    CONTINUE = "#continue"
    FINISH = "#finish"
    
    def start_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
    
    def fill_checkout_info(self, user:User):
        self.fill(self.FIRST_NAME,user.first_name)
        self.fill(self.LAST_NAME,user.last_name)
        self.fill(self.POSTAL_CODE,user.postal_code)
    
    def go_back_home(self):
        return self.page.locator("#back-to-products").click()
    
    def continue_checkout(self):
        self.click(self.CONTINUE)
    
    def finish_checkout(self):
        self.click(self.FINISH)

    def error_locator(self):
        return self.page.locator('[data-test="error"]')
    
    def complete_header(self):
        return self.page.locator(".complete-header")  
    