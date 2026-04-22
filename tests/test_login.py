from login_page import LoginPage
import pytest

def test_login(page):
    login = LoginPage(page)

    login.load()
    login.login("standard_user", "secret_sauce")
    # page.pause()

    assert login.is_logged_in()
    # assert "inventory" in page.url

def test_invalid_login(page):
    Login = LoginPage(page)
    Login.load()
    Login.login("wrong","wrong")
    assert "Epic sadface: Username and password do not match any user in this service" in page.content().lower()

def test_user_locked_out(page):
    Login = LoginPage(page)
    Login.load()
    Login.login("locked_out_user","secret_sauce")
    assert "locked out" in page.content().lower()


@pytest.mark.parametrize("username,password,expected",[
    ("standard_user", "secret_sauce", True),
    ("wrong", "wrong", False),
])
def test_login_cases(page,username,password,expected):
    login = LoginPage(page)
    login.load()
    login.login(username,password)
    assert login.is_logged_in() == expected
