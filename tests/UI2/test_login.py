from playwright.sync_api import Page

from page_objects.pages import LoginPage, HomePage


def test_login_successfully(page: Page):
    email = 'abc123@123.com'
    password = '123456'

    login_page = LoginPage(page)
    login_page.navigate()
    login_page.fill_email(email)
    login_page.fill_password(password)
    login_page.submit()

    home_page = HomePage(page)
    assert home_page.login_successfuly(), (
        'Failed to login.'
    )