from time import sleep

from behave import step

from models.models import get_fake
from pages import get_page_object
from steps import go_to_which_page, created, get_page_object


@step('that an item and a deposit were created')
def created_item_n_deposit(context):
    go_to_which_page(context, 'items')
    created(context, 'item')
    go_to_which_page(context, 'deposits')
    created(context, 'deposit')


@step('submit inventory fake data')
def submit_inventory(context):
    fake_data = get_fake('inventory')
    fake_data['item_name'] = context.item_name
    fake_data['deposit_name'] = context.deposit_name
    page_create = get_page_object('inventory', 'create', context.driver)
    for field, value in fake_data.items():
        eval(f'page_create.fill_{field}("{value}")')
    page_create.submit()


@step('create one inventory')
def create_inventory(context):
    page = get_page_object('inventory', 'all', context.driver)
    context.driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)
    page.click_new()
    submit_inventory(context)


@step('created one inventory')
def created_inventory(context):
    created_item_n_deposit(context)
    go_to_which_page(context, 'inventories')
    create_inventory(context)


@step('update inventory')
def update_inventory(context):
    page = get_page_object('inventory', 'detail', context.driver)
    page.edit()
    submit_inventory(context)
