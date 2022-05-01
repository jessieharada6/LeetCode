from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.size = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
            

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
            
        if self.size == len(self.cache):
            self.cache.popitem(last=False)
        
        self.cache[key] = value
            
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key) # tail item is the most recently used cache
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key] # key can be the same with diff val
        if len(self.cache) >= self.size:
            self.cache.popitem(last=False) # head item is the least recently used cache
        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)