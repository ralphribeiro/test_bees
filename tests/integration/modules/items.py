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


def make_a_valid_item() -> dict:
    """Make a valid item

    Returns:
        dict: valid item
    """
    return {
        'name': make_random_str(20),
        'height': make_randon_float(),
        'width': make_randon_float(),
        'weight': make_randon_float()
    }


def make_a_invalid_item() -> dict:
    """Make a invalid item

    Returns:
        dict: invalid item
    """
    return {
        'name': make_randon_float(),
        'height': make_random_str(20),
        'width': make_random_str(20),
        'weight': make_random_str(20)
    }


def check_if_changed_values(expected: dict, returned: dict) -> bool:
    """Check if item has updated

    Args:
        expected (dict): expected item values
        returned (dict): returned item

    Returns:
        bool: has changed
    """
    return all(returned[key] == str(value) for key, value in expected.items())
