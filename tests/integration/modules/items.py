from helpers.fakes import make_randon_float, make_random_str


def make_a_item(valid: bool = True) -> dict:
    """Make a item

    Args:
        valid (bool): if is valid

    Returns:
        dict: valid item
    """
    if valid:
        return {
            'name': make_random_str(20),
            'height': make_randon_float(),
            'width': make_randon_float(),
            'weight': make_randon_float()
        }
    return {
        'xxxxxx': make_randon_float(),
        'yyyyyy': make_random_str(20),
        'zzzzzz': make_random_str(20),
        'wwwwww': make_random_str(20)
    }
