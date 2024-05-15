#!/usr/bin/env python3
"""Function to implement a get_page using requests"""
import requests
import time
from typing import Callable
import redis
from functools import wraps


redis = redis.Redis()


def wrap_decorator(func: Callable) -> Callable:
    """Defines a decorator wrapper"""

    @wraps(func)
    def wrapper(url):
        """Defines a method to check if URL is in cache and not expired"""
        redis.incr(f"count:{url}")
        cached_response = redis.get(f"cached:{url}")
        if cached_response:
            return cached_response.decode('utf-8')
        content = func(url)
        redis.setex(f"cached:{url}", 10, content) 
        return content

    return wrapper


@wrap_decorators
def get_page(url: str) -> str:
    """Function to get HTML content of a particular URL"""
    response = requests.get(url)
    return response.text
