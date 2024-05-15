#!/usr/bin/env python3
"""Function to implement a get_page using requests"""
import requests
import time
import redis


redis_client = redis.StrictRedis()


def cache_decorator(func):
    def wrapper(url):
        """Defines a method to check if URL is in cache and not expired"""
        if url in cache and time.time() - cache[url]["timestamp"] < 10:
            cache[url]["count"] += 1
            return cache[url]["content"]

        content = func(url)

        cache[url] = {
            "content": content,
            "timestamp": time.time(),
            "count": 1
        }
        
        return content
    return wrapper


def get_page(url: str) -> str:
    """Function to get HTML content of a particular URL"""
    response = requests.get(url)
    return response.text
