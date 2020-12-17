from threading import Thread
from functools import wraps


def decorator(func):

    @wraps(func)
    def wrapper(*args, name, daemon):
        t = Thread(target=func, args=args, name=name, daemon=daemon)
        t.start()
        return t

    return wrapper
