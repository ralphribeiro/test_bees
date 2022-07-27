from random import choice, randint
from string import ascii_letters


def make_random_str(length: int) -> str:
    """Make a random string

    Args:
        length (int): string length

    Returns:
        str: random string
    """
    return ''.join(choice(ascii_letters) for _ in range(length))


def make_randon_float() -> float:
    """Make a random float

    Returns:
        float: random float
    """
    str_float = f'{randint(1, 1000)}.{randint(0, 99)}'
    return float(str_float)