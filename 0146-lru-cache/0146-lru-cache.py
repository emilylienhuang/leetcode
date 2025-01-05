class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
        print("Initialized OD with capacity " + str(self.capacity))

    def get(self, key: int) -> int:
        print("Getting from the cache")
        # check if dict or if key in dict
        if key in self.cache:
            val = self.cache.pop(key)
            self.cache[key] = val
            return val
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        if len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)