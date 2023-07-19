#!/usr/bin/env python3
'''module provides a simple and efficient way 
to cache and track requests using Redis,
which can be helpful for reducing 
the load on external servers and improving response 
times for frequently accessed URLs.'''

import redis
import requests
from functools import wraps
from typing import Callable


redis_cache = redis.Redis()
'''Connect to the Redis server.'''


def data_cacher(method: Callable) -> Callable:
    '''Caches the output of fetched data.'''
    @wraps(method)
    def invoker(url) -> str:
        '''The wrapper function for caching the output.'''
        redis_cache.incr(f'count:{url}')
        result = redis_cache.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_cache.set(f'count:{url}', 0)
        redis_cache.setex(f'result:{url}', 10, result)
        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    '''Returns the content of a URL after caching the request's response,
    and tracking the request'''
    return requests.get(url).text