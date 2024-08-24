#!/usr/bin/env python3
"""
Create a class FIFOCache that inherits from BaseCaching
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """
    class instantiation
    """
    def __init__(self):
        """
        initial instantiation
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

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD:", first_key)

    def get(self, key):
        """
        Retrieve items from cache
        """
        if key is None:
            return None
        else:
            return self.cache_data.get(key, None)
