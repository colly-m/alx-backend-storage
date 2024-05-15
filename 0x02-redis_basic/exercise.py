#!/usr/bin/env python3
"""
Module to create a cache
class storing a redis client as private variable
"""
import uuid
import redis
from typing import Union, Callable


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

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float, None]:
        """Defines a method to retrieve data stored in redis using a key
        and convetion results to desired format"""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Union[str, None]:
        """Defines a method to get a string"""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, None]:
        """Defines a method to get an int"""
        return self.get(key, int)
