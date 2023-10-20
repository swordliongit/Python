from dataclasses import dataclass

from functools import wraps


def decor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """example wrapper"""
        print(f"Adding headers..")
        func(*args, **kwargs)

    return wrapper


@decor
def func(i, j):
    """example func"""
    print(i + j)


func(5, 10)
print(func.__name__)
print(func.__doc__)
help(func)
