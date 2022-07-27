from behave import step


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
