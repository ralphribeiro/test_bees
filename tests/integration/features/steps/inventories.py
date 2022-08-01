import json

from behave import step
import requests

from helpers.tools import are_valids, is_valid
from modules.inventories import make_a_inventory


RESPONSE_FIELDS = (
    'id',
    'item_id',
    'deposit_id',
    'item_count',
    'created_at',
    'updated_at',
    'url'
)


@step('a list of valid inventories is returned')
def check_items_list(context):
    inventories = context.response.json()
    assert are_valids(inventories, RESPONSE_FIELDS), (
        '\nThere are invalid inventories in the returned list.'
    )


@step('make a valid inventory payload')
def make_inventory(context):
    item_id = getattr(context, 'item_id', 0)
    deposit_id = getattr(context, 'deposit_id', 0)
    inventory = make_a_inventory(deposit_id, item_id)
    context.inventory = inventory


@step('make a request to post inventory')
def post_inventory(context):
    url = context.root_url + 'inventories.json'
    headers = {'Content-Type': 'application/json'}
    context.response = requests.post(
        url, headers=headers, data=json.dumps(context.inventory)
    )


@step('a valid inventory is returned')
def check_inventory(context):
    inventory = context.response.json()
    assert is_valid(inventory, RESPONSE_FIELDS), (
        '\nInvalid inventory.'
    )


@step('make request to delete a inventory by id')
def delete_inventory(context):
    inventory_id = context.inventory_id
    url = f'{context.root_url}inventories/{inventory_id}.json'
    context.response = requests.delete(url)


@step('make a request to get inventory by "{type_}" id')
def post_deposit_with_items(context, type_):
    ids = {
        'valid': getattr(context, 'inventory_id', None),
        'invalid': 9999999999999999
    }
    url = f'{context.root_url}inventories/{ids[type_]}.json'
    context.response = requests.get(url)


@step('make request to update a inventory values with "{mode}"')
def update_inventory(context, mode):
    modes = {
        'patch': requests.patch,
        'put': requests.put
    }
    inventory_id = context.inventory_id
    deposit_id = context.deposit_id
    item_new_id = context.item_new_id
    to_modify_inventory = make_a_inventory(deposit_id, item_new_id)
    headers = {'Content-Type': 'application/json'}
    url = f'{context.root_url}inventories/{inventory_id}.json'
    context.response = modes[mode](
        url, headers=headers, data=json.dumps(to_modify_inventory)
    )
    context.new_inventory = to_modify_inventory
