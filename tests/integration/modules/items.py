from helpers.fakes import make_random_str, make_randon_float

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


def is_valid_item(item: dict) -> bool:
    """Check if item have all attributes

    Args:
        item (dict): item

    Returns:
        bool: is valid
    """
    return all(field in item for field in RESPONSE_FIELDS)


def is_valid_items(items: list[dict]) -> bool:
    """Check if all items valids

    Args:
        items (list[dict]): items list

    Returns:
        bool: all valids
    """
    return all(is_valid_item(item) for item in items)


def make_a_item(valid: bool=True) -> dict:
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
