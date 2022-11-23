class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        else:
            n = len(nums)
            l, r = 0, n - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] >= nums[0]:   # in part A
                    l = m + 1
                else:
                    r = m - 1
            
            return nums[l]