# dictionaries are ordered in python since 3.7, so you don't deed to use OrderedDict.

from collections import OrderedDict
from collections import defaultdict

class LFUCache:

    def __init__(self, capacity: int):
        self.cache = defaultdict(OrderedDict)
        self.freq = defaultdict(int)
        self.min = 1
        self.size = capacity

    def get(self, key: int) -> int:
        if key in self.freq:
            # get freq and val, remove current val
            freq = self.freq[key]
            val = self.cache[freq][key]
            del self.cache[freq][key]
            
            # update frequency and cache
            self.freq[key] += 1
            self.cache[freq + 1][key] = val
            
            # update min
            if self.min == freq and not self.cache[freq]:
                self.min += 1
            return val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.freq:
            # update value
            self.get(key)
            self.cache[self.freq[key]][key] = value
        else:
            self.size -= 1
            
            self.freq[key] = 1
            self.cache[1][key] = value
             
            if self.size < 0:           # no need to increment self.size, as we will never remove any elements 
                self.size = 0
                # remove first item with min freq
                k, v = self.cache[self.min].popitem(last=False)
                del self.freq[k]
                
            self.min = 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
class LFUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.freq = defaultdict(int) # freq
        self.cache = defaultdict(OrderedDict) # val - ordered by freq
        self.min_freq = 1

    def get(self, key: int) -> int:
        if key in self.freq:
            freq = self.freq[key] # initial freq
            val = self.cache[freq][key] # get val by initial    
            del self.cache[freq][key] # remove initial k-v pair
            
            self.freq[key] += 1 # increment current freq 
            self.cache[freq + 1][key] = val # add to the new k-v pair list
            
            if self.min_freq == freq and not self.cache[freq]: # update min_freq when the k-v pair no longer exists
                self.min_freq += 1
              
            return val
        return -1
         

    def put(self, key: int, value: int) -> None:
        if key in self.freq:
            self.get(key) # get the previous val
            self.cache[self.freq[key]][key] = value # update to the current val
        else:
            # new freq with new k-v pair
            self.size -= 1
            self.freq[key] = 1
            self.cache[1][key] = value
            
            if self.size < 0:
                self.size = 0
                # pop the first item in the list & min freq
                k, v = self.cache[self.min_freq].popitem(last=False) 
                del self.freq[k]
            
            self.min_freq = 1 # update the min freq as new item is added
            
        
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)