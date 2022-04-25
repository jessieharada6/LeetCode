import random
class RandomizedSet:

    def __init__(self):
        self.nums = [] # bottom container
        self.pos = {} # store index

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        
        # logic: new val will always be the last index
        self.nums.append(val)
        self.pos[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        # logic: replace last element with the val to be deleted at its position

        if val in self.pos:
            index = self.pos[val] # get index of the val
            last = self.nums[-1] # get last element
            
            # assign last element to the index to be deleted
            self.pos[last] = index 
            self.nums[index] = last 
            
            # remove last element
            self.nums.pop() 
            self.pos.pop(val) 
            return True
        
        return False

    def getRandom(self) -> int:
        return random.choice(self.nums)
        # return self.nums[random.randint(0, len(self.nums) - 1)]
            
        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()