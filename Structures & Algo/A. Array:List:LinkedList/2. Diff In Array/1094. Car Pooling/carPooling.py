class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:    
        n = 0
        for _, _, to in trips:
            if n < to:
                n = max(n, to)
        
        difference = [0 for _ in range(n)]
        
        for p, f, t in trips:
            difference[f] += p
            if t < n:
                difference[t] -= p
        
        passengers = 0
        for d in difference:
            passengers += d
            if passengers > capacity:
                return False
        
        return True


class DiffInArray:
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)
        self.diff = [0 for _ in range(self.n)]
    
    def difference(self):
        self.diff[0] = self.nums[0]
        for i in range(1, self.n):
            self.diff[i] = self.nums[i] - self.nums[i - 1]
    
    def increment(self, i, j, val):
        self.diff[i] += val
        if j + 1 < self.n:
            self.diff[j + 1] -= val
    
    def result(self):
        result = [0 for _ in range(self.n)]
        result[0] = self.diff[0]  
        for i in range(1, self.n):
            result[i] = self.diff[i] + result[i - 1]
        return result
    
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        df = DiffInArray([0 for i in range(1001)])
        
        for val, i, j in trips:
            # j is drop-off point
            df.increment(i, j - 1, val)     
        
        res = df.result()
        # print(res)
        for r in res:
            if r > capacity:
                return False
        
        return True