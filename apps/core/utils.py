"""Utility Functions for project-wide use"""

import random
import string


def generate_random_code(length: int = 5) -> str:
    """Generate a random code of digits of a given length"""
    start = 10 ** length
    end = 10 ** (length + 1) - 1
    return str(random.randint(start, end))


def generate_random_string(length: int = 5) -> str:
    """Generate a random string of letters of a given length"""
    return ''.join(random.choices(string.ascii_letters, k=length))
