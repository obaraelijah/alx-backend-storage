#!/usr/bin/env python
"""A module for using the Redis NoSQL data storage"""


import uuid
import redis
from typing import Any, Union, Callable


class Cache:
    """Create a Cache class"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb = True


    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate a random key"""
        random_data_key = str(uuid.uuid4())
        self._redis.set(random_data_key, data)
        return random_data_key

