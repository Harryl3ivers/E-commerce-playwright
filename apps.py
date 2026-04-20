import pytest
from playwright.sync_api import sync_playwright


with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge",headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.google.com")
        print("page title", page.title())
        browser.close()