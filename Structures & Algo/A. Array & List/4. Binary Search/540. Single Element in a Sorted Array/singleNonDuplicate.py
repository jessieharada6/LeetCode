# 考虑奇数下标或偶数下标
# true: 答案在右边
# false: 答案在左边
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 2
        
        while l <= r:
            m = (l + r) // 2
            if not m % 2:
                if nums[m + 1] != nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m - 1] != nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        
        return nums[l]
        
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        
        while l <= r:
            m = (l + r) // 2
            if m % 2:
                if m - 1 >= 0 and nums[m] == nums[m - 1]:
                    l = m + 1
                else:
                    r = m - 1 - 1
            else:
                if m + 1 < n and nums[m] == nums[m + 1]:
                    l = m + 1 + 1
                else:
                    r = m - 1
                    
        
        return nums[l]