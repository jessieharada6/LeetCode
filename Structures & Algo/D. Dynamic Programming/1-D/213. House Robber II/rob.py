class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def robHouse(start, end):
            a, b = 0, 0
            for i in range(start, end):
                a, b = b, max(nums[i] + a, b)
            return b  
            
        return max(robHouse(0, n - 1), robHouse(1, n)) if n != 1 else nums[0]