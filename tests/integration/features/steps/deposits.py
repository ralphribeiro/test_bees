import json

from behave import step
import requests


from modules.deposits import (
    is_valid_deposits,
    is_valid_deposit,
    make_a_valid_deposit
)


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


@step('a valid deposit')
def make_deposit(context):
    context.deposit = make_a_valid_deposit()


@step('make a request to post a valid deposit')
def post_deposit(context):
    url = context.root_url + 'deposits.json'
    headers = {
        'accept': '*/*',
        'Content-Type': 'application/json'
    }
    context.response = requests.post(
        url, headers=headers, data=json.dumps(context.deposit)
    )

@step('a valid deposit is returned')
def check_deposit(context):
    deposit = context.response.json()
    assert is_valid_deposit(deposit), (
        '\nInvalid deposit.'
    )