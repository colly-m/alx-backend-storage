#!/usr/bin/env python3
"""Function to implement a get_page using requests"""
import requests
import time
import redis


redis_client = redis.StrictRedis()

def get_page(url: str) -> str:
    """Defines a method to get a self descriptive page and returns the HTML contents"""
    cached_content = redis_client.get(url)
    if cached_content:
        return cached_content.decode('utf-8')

    response = requests.get(url)
    content = response.text

    redis_client.setex(url, 10, content)

    return content
