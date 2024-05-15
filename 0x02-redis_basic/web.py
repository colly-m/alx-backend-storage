#!/usr/bin/env python3
"""Function to implement a get_page using requests"""
import requests
import time
from typing import Callable
import redis
from functools import wraps


cache = {}


def cache_decorator(fn: Callable) -> Callable:
    """Defines a decorator wrapper"""

    @wraps(fn)
    def wrapper(url):
        """Defines a method to check if URL is in cache and not expiration"""
        if url in cache and time.time() - cache[url]["timestamp"] < 10:
            cache[url]["count"] += 1
            return cache[url]["content"]

        content = fn(url)

        cache[url] = {
            "content": content,
            "timestamp": time.time(),
            "count": 1
        }
        return content

    return wrapper


@cache_decorators
def get_page(url: str) -> str:
    """Function to get HTML content of a particular URL"""
    response = requests.get(url)
    return response.text
