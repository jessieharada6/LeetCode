class DiffInArray:
    
    # build diff array
    def __init__(self, nums):
        self.nums = nums
        self.n = len(self.nums)
        self.diff = [0 for i in range(self.n)]
    
    def diff(self):
        self.diff[0] = self.nums[0]
        for i in range(1, self.n):
            self.diff[i] = self.nums[i] - self.nums[i - 1]
    
    # can add or subtract val in range of [i,j]
    def increment(self, i, j, val):
        self.diff[i] += val
        if j + 1 < self.n:
            # note
            self.diff[j + 1] -= val
    
    # use diff array to get initial array
    def result(self):
        res = [0 for i in range(self.n)]
        res[0] = self.diff[0]
        for i in range(1, self.n):
            res[i] = self.diff[i] + res[i - 1]
        
        return res
            

class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        nums = [0] * length
        df = DiffInArray(nums)
        df.diff()
        
        for update in updates:
            i = update[0]
            j = update[1]
            val = update[2]
            df.increment(i, j, val)
        
        return df.result()

solution = Solution()
output = solution.getModifiedArray(5, [[1,3,2],[2,4,3],[0,2,-2]])
print(output)
