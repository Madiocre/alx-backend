#!/usr/bin/python3
""" BaseCaching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key == None or item == None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key == None or key not in self.cache_data.keys():
            return None
        
        return self.cache_data[key]