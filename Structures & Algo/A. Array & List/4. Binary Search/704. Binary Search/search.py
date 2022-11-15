class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        ans = n
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                ans = m
                r = m - 1
        
        if ans == n:
            return -1
        if nums[ans] != target:
            return -1
        return ans


# not binary search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        
        while i < len(nums):
            if nums[i] == target:
                return i
            i += 1
        
        return -1