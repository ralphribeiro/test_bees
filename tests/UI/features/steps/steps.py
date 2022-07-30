from behave import step

from helpers.models import get_fake
from pages import get_page_object
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

    assert context.driver.current_url != url, (
        '\nCould not login.'
    )


@step('that it is on the "{which}" page')
def go_to_which_page(context, which):
    login(context)
    endpoint = f'{context.root_url}/{which}'
    context.driver.get(endpoint)
    assert context.driver.current_url == endpoint, (
        '\nCould not go to items page.'
    )


@step('navigate to "{which}" create page')
def go_to_create(context, which):
    page = get_page_object(which, 'all', context.driver)
    page.click_new()


@step('submit "{which}" fake data')
def submit_create(context, which):
    page = get_page_object(which, 'create', context.driver)
    fake_data = get_fake(which)
    for field, value in fake_data.items():
        eval(f'page.fill_{field}("{value}")')
    page.submit()


@step('create one "{which}"')
def create_one(context, which):
    go_to_create(context, which)
    submit_create(context, which)


@step('"{which}" has created')
def check_created(context, which):
    page = get_page_object(which, 'detail', context.driver)
    message = page.get_success_message()
    expected = f'{which.capitalize()} was successfully created.'
    assert message == expected, '\nThe item was not created.'


@step('created one "{which}"')
def created(context, which):
    create_one(context, which)
    check_created(context, which)


@step('delete the created "{which}"')
def defete(context, which):
    ...
