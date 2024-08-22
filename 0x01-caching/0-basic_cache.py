#!/usr/bin/env python3
"""
class 2 use paren
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    class instantiation
    """
    def __init__(self):
        """
        initial instantiation
        """
        super().__init__()

    def put(self, key, item):
        """
        put item into cache
        """
        if key is None:
            raise ValueError("key is null")
        if item is None:
            raise ValueError("item is NULL")
        if len(self.cache_data) >= self.MAX_ITEMS:
            print("Cache is full, consider removing an item")
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve items from cache
        """
        if key is None:
            return None
        else:
            return self.cache_data.get(key)
