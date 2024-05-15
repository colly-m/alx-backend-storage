#!/usr/bin/env python3
"""
Module to create a cache
class storing a redis client as private variable
"""
import uuid
import redis
from typing import Union, Callable, Optional
from functools import wraps
import sys


def count_calls(method: Callable) -> Callable:
    """Defines a method to count the times a cache class is called"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Defines a wrap method of the cache class"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper

def call_history(method: Callable) -> Callable:
    """
    Defines a method to add its input parameters to one list
    in redis, and store its output into another list
    """
    key = method.__qualname__
    i = "".join([key, ":inputs"])
    o = "".join([key, ":outputs"])

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Defines a method to wrap of caches class"""
        self._redis.rpush(i, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(o, str(res))
        return result

    return wrapper


class Cache:
    """Class to store a method that takes a data arg and returns a string
    in caching system
    """

    def __init__(self):
        """Instance of Redis database"""
        self._redis = redis.Redis()
        self._redis.flushdb()


    @count_calls
    @call_history
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


def replay(method: Callable):
    """
    Defines a method to display the history of calls of a particular function.
    """
    key = method.__qualname__ + ":inputs"
    key_outputs = method.__qualname__ + ":outputs"

    inputs = redis_client.lrange(key_inputs, 0, -1)
    outputs = redis_client.lrange(key_outputs, 0, -1)

    print(f"{method.__qualname__} was called {len(inputs)} times:")
    for input_data, output_data in zip(inputs, outputs):
        print(f"{method.__qualname__}(*{input_data.decode('utf-8')}) -> {output_data.decode('utf-8')}")
