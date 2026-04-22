import pytest
from playwright.sync_api import sync_playwright
import os
from login_page import LoginPage
from utils.config import BASE_URL, STANDARD_USERNAME, PASSWORD
print("LOADING CONFTEST")
@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            channel="msedge",
            headless=False
        )
        context = browser.new_context()
        page = context.new_page()

        yield page

        context.close()
        browser.close()



os.makedirs("screenshots", exist_ok=True)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)

        if page:
            try:
                if not page.is_closed():
                    page.screenshot(path=f"screenshots/{item.name}.png")
            except Exception as e:
                print(f"[WARN] Screenshot failed: {e}")

@pytest.fixture
def login_page_auto(page):
    login_page = LoginPage(page)
    login_page.load()
    page.pause()
    login_page.login(STANDARD_USERNAME,PASSWORD)
    return page