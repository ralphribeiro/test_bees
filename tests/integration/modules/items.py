from random import choice, random
from string import ascii_letters


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


def make_random_str(length: int) -> str:
    """Make a random string

    Args:
        length (int): string length

    Returns:
        str: random string
    """
    return ''.join(choice(ascii_letters) for _ in range(length))


def make_a_valid_item() -> dict:
    """Make a valid item

    Returns:
        dict: valid item
    """
    return {
        'name': make_random_str(20),
        'height': random(),
        'width': random(),
        'weight': random()
    }
