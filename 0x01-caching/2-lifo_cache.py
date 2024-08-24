#!/usr/bin/env python3
"""
Create a class LIFOCache that inherits from BaseCaching
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """
    created LIFO class
    """
    def __init__(self):
        """
        class & method instantiation
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        put item into cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.pop(key)

        self.cache_data[key] = item

        if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
            last_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD:", last_key)

    def get(self, key):
        """
        Retrieve items from cache
        """
        if key is None:
            return None
        else:
            return self.cache_data.get(key, None)
