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
    
    def order_complete(self):
        return self.page.locator(".complete-header").inner_text()
    
    def has_error(self):
        error = self.page.locator('[data-test="error"]')
    
        try:
            expect(error).to_be_visible(timeout=2000)
            return True
        except:
            return False

    def get_error_message(self):
        error = self.page.locator('[data-test="error"]')
        expect(error).to_be_visible()
        return error.inner_text()
    
    