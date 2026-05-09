from pages.login_page import LoginPage
import pytest
from utils.config import STANDARD_USERNAME,PASSWORD

def test_login(page):
    login = LoginPage(page)

    login.load()
    login.login(STANDARD_USERNAME,PASSWORD)
    

    assert login.is_logged_in()
    # assert "inventory" in page.url

def test_invalid_login(page):
    login = LoginPage(page)
    login.load()
    login.login("wrong","wrong")
    assert "Epic sadface: Username and password do not match any user in this service" in page.content()

def test_user_locked_out(page):
    login = LoginPage(page)
    login.load()
    login.login("locked_out_user",PASSWORD)
    assert "locked out" in page.content().lower()


@pytest.mark.parametrize("username,password,expected",[
    (STANDARD_USERNAME, PASSWORD, True),
    ("wrong", "wrong", False),
])
def test_login_cases(page,username,password,expected):
    login = LoginPage(page)
    login.load()
    login.login(username,password)
    assert login.is_logged_in() == expected
