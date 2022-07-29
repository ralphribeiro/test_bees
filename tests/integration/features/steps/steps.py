from behave import step
import requests


INVALID_ID = 99999999999999999


@step('the test-bees url')
def get_test_bee_url(context):
    context.root_url = 'https://test-bees.herokuapp.com/'


@step('the status_code is "{status}"')
def chech_status_code(context, status):
    response = context.response
    status_code = str(response.status_code)
    assert status_code == status, (
        '\nFailed to request all items.'
        f'\nExpected: {status}'
        f'\nReturned: {status_code}'
    )


@step('make a request to get all "{which}"')
def get_all(context, which):
    url = f'{context.root_url}{which}.json'
    context.response = requests.get(url)


@step('save the "{which}" id')
def save_id(context, which):
    if response := getattr(context, 'response', None):
        setattr(context, f'{which}_id', response.json().get('id'))
    else:
        setattr(context, f'{which}_id', INVALID_ID)
