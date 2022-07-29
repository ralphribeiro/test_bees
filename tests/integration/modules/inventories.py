from random import randint


def make_a_inventory(
    deposit_id: int,
    item_id: int,
    valid: bool = True
) -> dict:
    """Make a inventory

    Args:
        deposit_id (int): deposit id
        item_id (Sequence): items ids
        valid (bool, optional): if is valid. Defaults to True.

    Returns:
        dict: inventory
    """
    if valid:
        return {
            "item_id": item_id,
            "deposit_id": deposit_id,
            "item_count": randint(1, 100)
        }
    return {
        "xxxxxxxxxx": 0,
        "yyyyyyyyyy": 0,
        "zzzzzzzzzz": 0
    }
