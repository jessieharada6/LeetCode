class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        # l and r may overlap, let l <= r
        while l <= r:
            # // floor division
            # r + (l - r) // 2 (instead of (l + r) // 2) to avoid overflow
            m = r + (l - r) // 2

            # use m as the point to determine if target is in the list
            if nums[m] == target:
                return m
            
            # left hand side is sorted
            if nums[l] <= nums[m]: 
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                # not in the range, l increase so that m can increase
                else:
                    l = m + 1
            # right hand side is sorted
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
                
            
        return -1