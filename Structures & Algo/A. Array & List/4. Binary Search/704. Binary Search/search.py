class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = floor(l + (r - l) / 2)
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            elif nums[m] == target:
                return m
        
        return -1


# not binary search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        
        while i < len(nums):
            if nums[i] == target:
                return i
            i += 1
        
        return -1