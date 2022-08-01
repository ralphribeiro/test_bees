from behave import step

from pages.home import HomePage
from pages.login import LoginPage


@step('has authenticated')
def login(context):
    url = 'https://test-bees.herokuapp.com/users/sign_in'
    context.driver.get(url)

    email = 'abc123@123.com'
    password = '123456'

    login_page = LoginPage(context.driver)
    login_page.fill_email(email)
    login_page.fill_password(password)
    login_page.submit()

    home_page = HomePage(context.driver)
    message = home_page.get_success_login_message()

    assert message == 'Signed in successfully.', (
        '\nCould not login.'
    )


@step('logout')
def logout(context):
    page = HomePage(context.driver)
    page.logout()
