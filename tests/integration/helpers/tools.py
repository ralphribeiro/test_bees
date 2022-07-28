def check_if_changed_values(expected: dict, returned: dict) -> bool:
    """Check if item has updated

    Args:
        expected (dict): expected item values
        returned (dict): returned item

    Returns:
        bool: has changed
    """
    return all(returned[key] == str(value) for key, value in expected.items())