from base_page import BasePage
from utils.config import BASE_URL
from playwright.sync_api import sync_playwright

class LoginPage(BasePage):

    def load(self):
        print("[DEBUG] Navigating to login page")
        self.navigate(BASE_URL)

    def login(self, user, password):
        print(f"[DEBUG] Entering username: {user}")
        self.fill("#user-name", user)

        print("[DEBUG] Entering password")
        self.fill("#password", password)

        print("[DEBUG] Clicking login button")
        self.click("#login-button")

    def is_logged_in(self) -> bool:
        current_url = self.page.url
        print(f"[DEBUG] Current URL after login: {current_url}")
        return "inventory" in current_url
    

