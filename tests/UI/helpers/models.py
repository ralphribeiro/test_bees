from faker import Faker


def get_fake(which: str) -> dict:
    """Get fake object

    Args:
        which (str): which object

    Returns:
        dict: fakes
    """
    faker = Faker()
    fakes = {
        'item': {
            'name': faker.word(),
            'height': faker.numerify('!!!%,%%'),
            'width': faker.numerify('!!!%,%%'),
            'weight': faker.numerify('!!!%,%%')
        },
        'deposit': {
            'name': faker.name(),
            'address': faker.street_name(),
            'city': faker.city(),
            'state': faker.state(),
            'zipcode': faker.zipcode()
        }
    }
    return fakes[which]
