# simplified solution
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        result = [0 for _ in range(n)]
        difference = [0 for _ in range(n)]
        
        for first, last, seats in bookings:
            if first - 1 >= 0:
                difference[first - 1] += seats
            if last < n:
                difference[last] -= seats
        

        result[0] = difference[0]
        
        for i in range(1, n):
            result[i] = difference[i] + result[i - 1]
            
        return result


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