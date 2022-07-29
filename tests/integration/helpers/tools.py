from typing import Sequence


def check_if_changed_values(expected: dict, returned: dict) -> bool:
    """Check if item has updated

    Args:
        expected (dict): expected item values
        returned (dict): returned item

    Returns:
        bool: has changed
    """
    return all(returned[key] == str(value) for key, value in expected.items())


def is_valid(which: dict, fields: Sequence) -> bool:
    """Check if which have all attributes

    Args:
        which (dict): which
        fields (Sequence): fields to validate

    Returns:
        bool: is valid
    """
    return all(field in which for field in fields)


def are_valids(whichs: list[dict], fields: Sequence) -> bool:
    """Check if all items valids

    Args:
        whichs (list[dict]): which list
        fields (Sequence): fields to validate

    Returns:
        bool: all valids
    """
    return all(is_valid(which, fields) for which in whichs)