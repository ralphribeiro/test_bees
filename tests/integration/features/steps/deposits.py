import json

from behave import step
import requests

from helpers.tools import check_if_changed_values
from modules.deposits import (
    is_valid_deposits,
    is_valid_deposit,
    make_a_deposit
)


INVALID_ID = 99999999999999999


@step('make a request to get all deposits')
def get_all_deposits(context):
    url = context.root_url + 'deposits.json'
    context.response = requests.get(url)


@step('a list of valid deposits is returned')
def check_deposits_list(context):
    deposits = context.response.json()
    assert is_valid_deposits(deposits), (
        '\nThere are invalid deposits in the returned list.'
    )


@step('a "{value}" deposit')
def make_deposit(context, value):
    param = {
        "valid": True,
        "invalid": False
    }
    context.deposit = make_a_deposit(param[value])


@step('make a request to post deposit')
def post_deposit(context):
    url = context.root_url + 'deposits.json'
    headers = {'Content-Type': 'application/json'}
    context.response = requests.post(
        url, headers=headers, data=json.dumps(context.deposit)
    )


@step('make a request to get deposit by "{type_}" id')
def post_deposit_with_items(context, type_):
    ids = {
        'valid': getattr(context, 'deposit_id', None),
        'invalid': INVALID_ID
    }
    url = f'{context.root_url}deposits/{ids[type_]}.json'
    context.response = requests.get(url)


@step('a valid deposit is returned')
def check_deposit(context):
    deposit = context.response.json()
    assert is_valid_deposit(deposit), (
        '\nInvalid deposit.'
    )


@step('save the deposit id')
def save_id(context):
    if response := getattr(context, 'response', None):
        context.deposit_id = response.json().get('id')
    else:
        context.deposit_id = INVALID_ID


@step('make request to update a deposit values with "{mode}"')
def update_deposit(context, mode):
    modes = {
        'patch': requests.patch,
        'put': requests.put
    }
    old_deposit_id = context.deposit_id
    new_deposit = make_a_deposit()
    headers = {'Content-Type': 'application/json'}
    url = f'{context.root_url}deposits/{old_deposit_id}.json'
    context.response = modes[mode](
        url, headers=headers, data=json.dumps(new_deposit)
    )
    context.new_deposit = new_deposit

@step('deposit values has changed')
def check_changed_values(context):
    expected = context.new_deposit
    returned = context.response.json()
    assert check_if_changed_values(expected, returned), (
        '\nThe deposit has not been updated'
        f'\nExpected: {expected}'
        f'\nReturned: {returned}'
    )



@step('make request to delete a deposit by id')
def delete_deposit(context):
    deposit_id = context.deposit_id
    url = f'{context.root_url}deposits/{deposit_id}.json'
    context.response = requests.delete(url)
