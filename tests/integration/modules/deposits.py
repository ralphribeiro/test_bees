from helpers.fakes import make_randon_float, make_random_str


def make_a_deposit(valid: bool=True) -> dict:
    """Make a valid deposit

    Args:
        valid (bool): if is valid

    Returns:
        dict: valid deposit
    """
    if valid:
        return {
            'name': make_random_str(20),
            'address': make_random_str(20),
            'city': make_random_str(20),
            'state': make_random_str(20),
            'zipcode': make_random_str(20)
        }
    return {
        'xxxxxx': make_randon_float(),
        'yyyyyy': make_random_str(20),
        'zzzzzz': make_random_str(20),
        'wwwwww': make_random_str(20)
    }
