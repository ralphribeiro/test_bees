from playwright.sync_api import Page


class LoginPage:
    endpoint = 'https://test-bees.herokuapp.com/users/sign_in'

    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator('id=user_email')
        self.password_input = page.locator('id=user_password')
        self.submit_button = page.locator('.btn')

    def navigate(self):
        self.page.goto(self.endpoint)

    def fill_email(self, text):
        self.email_input.fill(text)

    def fill_password(self, text):
        self.password_input.fill(text)

    def submit(self):
        self.submit_button.click()


class HomePage:
    endpoint = 'https://test-bees.herokuapp.com'

    def __init__(self, page: Page):
        self.page = page
        self.successfully = page.locator('text=Signed in successfully.')

