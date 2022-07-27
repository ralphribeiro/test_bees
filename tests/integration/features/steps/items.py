import json

from behave import step
import requests

from modules.items import is_valid_items, make_a_valid_item


@step('the test-bees url')
def get_test_bee_url(context):
    context.root_url = 'https://test-bees.herokuapp.com/'


@step('make a request to get all items')
def get_all_items_request(context):
    url = context.root_url + 'items.json'
    context.response = requests.get(url)


@step('the status_code is "{status}"')
def chech_status_code(context, status):
    response = context.response
    status_code = str(response.status_code)
    assert status_code == status, (
        '\nFailed to request all items.'
        f'\nExpected: {status}'
        f'\nReturned: {status_code}'
    )
    context.response_items = response.json()


@step('a list of valid items is returned')
def check_items_list(context):
    items = context.response_items
    assert is_valid_items(items), (
        '\nThere are invalid items in the returned list.'
    )


@step('a valid item')
def make_item(context):
    context.item = make_a_valid_item()


@step('make a request to post a valid item')
def post_item(context):
    url = context.root_url + 'items.json'
    headers = {
        'accept': '*/*',
        'Content-Type': 'application/json'
    } 
    context.response = requests.post(
        url, headers=headers,data=json.dumps(context.item)
    )
