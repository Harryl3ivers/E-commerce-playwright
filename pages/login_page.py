from pages.base_page import BasePage
from utils.config import BASE_URL,STANDARD_USERNAME,PASSWORD

class LoginPage(BasePage):

    def load(self):
        self.navigate(BASE_URL)

    def login(self, STANDARD_USERNAME, PASSWORD):
        self.fill("#user-name", STANDARD_USERNAME)
        self.fill("#password", PASSWORD)
        self.click("[data-test^='login-button']")
    
    def open_menu(self):
        self.click("#react-burger-menu-btn")
    
    def logout(self):
        self.click("#logout_sidebar_link")

    def is_logged_in(self) -> bool:
        current_url = self.page.url
        return "inventory" in current_url
    

