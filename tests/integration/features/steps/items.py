import json

from behave import step
import requests

from helpers.tools import check_if_changed_values
from modules.items import (
    is_valid_item,
    is_valid_items,
    make_a_invalid_item,
    make_a_valid_item
)


@step('make a request to get all items')
def get_all_items(context):
    url = context.root_url + 'items.json'
    context.response = requests.get(url)


@step('a list of valid items is returned')
def check_items_list(context):
    items = context.response.json()
    assert is_valid_items(items), (
        '\nThere are invalid items in the returned list.'
    )


@step('a valid item')
def make_item(context):
    context.item = make_a_valid_item()


@step('a invalid item')
def make_invalid_item(context):
    context.item = make_a_invalid_item()


@step('make a request to post a valid item')
def post_item(context):
    url = context.root_url + 'items.json'
    headers = {'Content-Type': 'application/json'}
    context.response = requests.post(
        url, headers=headers, data=json.dumps(context.item)
    )


@step('a valid item is returned')
def check_item(context):
    item = context.response.json()
    assert is_valid_item(item), (
        '\nInvalid item.'
    )


@step('save the item id')
def save_id(context):
    context.item_id = context.response.json().get('id')


@step('make a request to get item by id')
def get_item_by_id(context):
    url = f'{context.root_url}items/{context.item_id}.json'
    context.response = requests.get(url)


@step('make request to update a item values with "{mode}"')
def update_item(context, mode):
    modes = {
        'patch': requests.patch,
        'put': requests.put
    }
    old_item_id = context.item_id
    new_item = make_a_valid_item()
    headers = {'Content-Type': 'application/json'}
    url = f'{context.root_url}items/{old_item_id}.json'
    context.response = modes[mode](
        url, headers=headers, data=json.dumps(new_item)
    )
    context.new_item = new_item


@step('item values has changed')
def check_changed_values(context):
    expected = context.new_item
    returned = context.response.json()
    assert check_if_changed_values(expected, returned), (
        '\nThe item has not been updated'
        f'\nExpected: {expected}'
        f'\nReturned: {returned}'
    )


@step('make request to delete a item by id')
def delete_item(context):
    item_id = context.item_id
    url = f'{context.root_url}items/{item_id}.json'
    context.response = requests.delete(url)
