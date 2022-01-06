class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # left biased to find the most left
        left = self.binarySearch(nums, target, True)
        # right biased to find the most right
        right = self.binarySearch(nums, target, False)
        return [left, right]
    
    def binarySearch(self, nums, target, left_biased):
        l = 0
        r = len(nums) - 1
        i = -1
        
        while l <= r:
            m = l + (r - l) // 2
            
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                i = m
                # look for the most left index
                # push right boundary to the left
                if left_biased:
                    r = m - 1
                else:
                    l = m + 1
        
        return i