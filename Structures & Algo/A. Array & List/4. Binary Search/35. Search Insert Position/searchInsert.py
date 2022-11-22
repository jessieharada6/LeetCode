class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return l

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        ans = n    
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                ans = m
                r = m - 1
        
        return ans


# it is a question about searching the left boundary
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def searchLeft():
            l = 0
            r = len(nums) - 1
            
            while l <= r:
                m = l + floor((r - l) / 2)
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                elif nums[m] == target:
                    r = m - 1
            return l
        
        return searchLeft()
        
        
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        if target < nums[l]:
            return 0
        if target > nums[r]:
            return len(nums)
        
        ans = 0
        
        while l <= r:
            m = l + floor((r - l)/2)
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            elif nums[m] == target:
                return m
        
        return l
        
        