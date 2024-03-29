class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 2
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] >= nums[m + 1]:    # T: ans is m itself or ans is at m's left
                r = m - 1
            else:
                l = m + 1
        return l

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 2
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] < nums[m + 1]:
                l = m + 1
            else:
                r = m - 1
        
        return l