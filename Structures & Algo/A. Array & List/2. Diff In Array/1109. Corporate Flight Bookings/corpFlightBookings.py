# simplified solution
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0 for _ in range(n)]
        ans = [0 for _ in range(n)]
        
        for f, l, s in bookings:
            diff[f - 1] += s                # not needed to check f - 1 >= 0, as f starts from 1
            if l < n:
                diff[l] -= s
        
        ans[0] = diff[0]
        for i in range(1, n):
            ans[i] += ans[i - 1] + diff[i]

        return ans


# original class
class DiffInArray: 
    def __init__(self, nums):
        self.nums = nums
        self.n = len(self.nums)
        self.diff = [0 for i in range(self.n)]
    
    def diff(self):
        self.diff[0] = self.nums[0]
        for i in range(1, self.n):
            self.diff[i] = self.nums[i] - self.nums[i - 1]
    
    def increment(self, i, j, val):
        self.diff[i] += val
        if j + 1 < self.n:
            self.diff[j + 1] -= val
    
    def result(self):
        result = [0 for i in range(self.n)]
        result[0] = self.diff[0]
        for i in range(1, self.n):
            result[i] = self.diff[i] + result[i - 1]
        return result
    
    
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        df = DiffInArray([0] * n)
        
        for booking in bookings:
            i = booking[0] - 1
            j = booking[1] - 1 
            val = booking[2]
            df.increment(i, j, val)
        
        return df.result()