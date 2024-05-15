#!/usr/bin/env python3
"""
Module to create a cache
class storing a redis client as private variable
"""
import uuid
import redis
from typing import Union


class Cache:
    """Class to store a method that takes a data arg and returns a string
    in caching system
    """

    def __init__(self):
        """Instance of Redis database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Defines a method to take data then return a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
