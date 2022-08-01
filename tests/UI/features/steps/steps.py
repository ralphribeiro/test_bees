from time import sleep

from behave import step

from models.models import get_fake
from pages import get_page_object


@step('go to the "{which}" page')
@step('that it is on the "{which}" page')
def go_to_which_page(context, which):
    endpoint = f'{context.root_url}/{which}'
    context.driver.get(endpoint)
    assert context.driver.current_url == endpoint, (
        f'\nCould not go to {which} page.'
    )


@step('navigate to "{which}" create page')
def go_to_create(context, which):
    page = get_page_object(which, 'all', context.driver)
    context.driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)
    page.click_new()


@step('submit "{which}" fake data')
def submit_create(context, which):
    page = get_page_object(which, 'create', context.driver)
    fake_data = get_fake(which)
    for field, value in fake_data.items():
        eval(f'page.fill_{field}("{value}")')
    page.submit()


@step('save "{which}" name')
def save_name(context,  which):
    page = get_page_object(which, 'detail', context.driver)
    try:
        name = page.get_name()
    except AttributeError:
        ...
    else:
        name = name.split(': ')[1]
        setattr(context, f'{which}_name', name)


@step('create one "{which}"')
def create_one(context, which):
    go_to_create(context, which)
    submit_create(context, which)
    save_name(context, which)


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


@step('destroy the created "{which}"')
def delete(context, which):
    page = get_page_object(which, 'detail', context.driver)
    page.delete()


@step('"{which}" has destroyed')
def check_destroyed(context, which):
    page = get_page_object(which, 'all', context.driver)
    message = page.get_success_destroyed_message()
    expected = f'{which.capitalize()} was successfully destroyed.'
    assert message == expected, '\nThe item was not destroyed.'


@step('"{which}" has updated')
def check_updated(context, which):
    page = get_page_object(which, 'detail', context.driver)
    message = page.get_success_message()
    expected = f'{which.capitalize()} was successfully updated.'
    assert message == expected, '\nThe item was not updated.'


@step('update "{which}"')
def update(context, which):
    page = get_page_object(which, 'detail', context.driver)
    page.edit()
    submit_create(context, which)
    check_updated(context, which)
