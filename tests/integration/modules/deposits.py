from helpers.fakes import make_random_str


RESPONSE_FIELDS = [
    'id',
    'name',
    'address',
    'city',
    'state',
    'zipcode',
    'created_at',
    'updated_at',
    'items',
    'url'
]


def is_valid_deposit(deposit: dict) -> bool:
    """Check if deposit have all attributes

    Args:
        deposit (dict): deposit

    Returns:
        bool: is valid
    """
    return all(field in deposit for field in RESPONSE_FIELDS)


def is_valid_deposits(deposits: list[dict]) -> bool:
    """Check if all deposits valids

    Args:
        deposits (list[dict]): deposits list

    Returns:
        bool: all valids
    """
    return all(is_valid_deposit(deposit) for deposit in deposits)


def make_a_valid_deposit() -> dict:
    """Make a valid deposit

    Returns:
        dict: valid deposit
    """
    return {
        'name': make_random_str(20),
        'address': make_random_str(20),
        'city': make_random_str(20),
        'state': make_random_str(20),
        'zipcode': make_random_str(20)
    }
