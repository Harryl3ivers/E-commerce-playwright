from login_page import LoginPage

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
    assert "error" in page.content().lower()