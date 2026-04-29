from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self,page: Page):
        self.page = page
    
    def navigate(self, url):
        self.page.goto(url)
    
    def click(self, selector):
         element = self.page.locator(selector)
         expect(element).to_be_visible()
         element.click()
        

    def fill(self, selector, text):
        element = self.page.locator(selector)
        expect(element).to_be_visible(timeout=5000)
        element.fill(text)

    def get_count(self,selector:str):
        return self.page.locator(selector).count()
    
    def get_text(self, selector:str):
        element = self.page.locator(selector)
        expect(element).to_be_visible()
        return element.inner_text()
    
    
    def is_visible(self,selector) -> bool:
        return self.page.locator(selector).is_visible()