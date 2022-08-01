import json

from behave import step
import requests

from helpers.tools import are_valids, check_if_changed_values, is_valid
from modules.items import make_a_item


RESPONSE_FIELDS = (
    'id',
    'name',
    'height',
    'width',
    'weight',
    'created_at',
    'updated_at',
    'url',
)


@step('a list of valid items is returned')
def check_items_list(context):
    items = context.response.json()
    assert are_valids(items, RESPONSE_FIELDS), (
        '\nThere are invalid items in the returned list.'
    )


@step('a "{value}" item')
def make_item(context, value):
    param = {
        "valid": True,
        "invalid": False
    }
    context.item = make_a_item(param[value])


@step('make a request to post item')
def post_item(context):
    url = context.root_url + 'items.json'
    headers = {'Content-Type': 'application/json'}
    context.response = requests.post(
        url, headers=headers, data=json.dumps(context.item)
    )


@step('a valid item is returned')
def check_item(context):
    item = context.response.json()
    assert is_valid(item, RESPONSE_FIELDS), (
        '\nInvalid item.'
    )


@step('make a request to get item by "{type_}" id')
def get_item_by_id(context, type_):
    ids = {
        'valid': getattr(context, 'item_id', None),
        'invalid': 9999999999999999
    }
    url = f'{context.root_url}items/{ids[type_]}.json'
    context.response = requests.get(url)


@step('make request to update a item values with "{mode}"')
def update_item(context, mode):
    modes = {
        'patch': requests.patch,
        'put': requests.put
    }
    old_item_id = context.item_id
    new_item = make_a_item()
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
def delete_new_item(context):
    item_id = context.item_id
    url = f'{context.root_url}items/{item_id}.json'
    context.response = requests.delete(url)


@step('make request to delete a new item by id')
def delete_item(context):
    item_id = context.item_new_id
    url = f'{context.root_url}items/{item_id}.json'
    context.response = requests.delete(url)
