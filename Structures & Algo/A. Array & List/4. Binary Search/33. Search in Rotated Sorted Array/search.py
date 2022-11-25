class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find min
        n = len(nums)
        l, r = 0, n - 2
        while l <= r:
            m = (l + r) // 2
            if nums[m] >= nums[-1]:
                l = m + 1
            else:
                r = m - 1
        minPos = l
        
        l, r = 0, n - 1
        if target <= nums[-1]:      # part B
            l = minPos
        else:
            r = minPos - 1          # part A
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        if nums[l] != target:
            return -1
        return l
        
        

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        minPos = 0
        
        if nums[0] > nums[-1]:        # rotated array
            # find min
            l, r = 0, n - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] >= nums[0]: # currently in part A
                    l = m + 1          # go to part B
                else:
                    r = m - 1
            minPos = l
        
        l, r = 0, n - 1
        if nums[minPos] <= target < nums[0]:
            l = minPos
        if minPos != 0 and nums[0] <= target <= nums[minPos - 1]:
            r = minPos - 1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        if l == n or nums[l] != target:
            return -1
        return l


# ----------------------------------------------------------------
# m in part A
    # target in part A : binary search
    # target in part B: l = m + 1
# m in part b
    # target in part B : binary search
    # target in part A: r = m - 1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[-1]:  # part A
                if target <= nums[-1] or (target > nums[-1] and nums[m] < target): # part B
                    l = m + 1
                else:
                    # if nums[m] < target:
                    #     l = m + 1
                    # else:
                    r = m - 1
            else:
                if target > nums[-1] or (target <= nums[-1] and nums[m] >= target):
                    r = m - 1
                else:
                    l = m + 1
                    # if nums[m] < target:
                    #     l = m + 1
                    # else:
                    #     r = m - 1
        
        if nums[l] != target:
            return -1
        return l
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] < nums[0]: # m in part B
                if nums[0] <= target: # target in part A
                    r = m - 1
                else:
                    if nums[m] < target:
                        l = m + 1
                    else:
                        r = m - 1
            else:                  # m in part A
                if nums[0] > target: # target in part B
                    l = m + 1
                else:
                    if nums[m] < target:
                        l = m + 1
                    else:
                        r = m - 1
        
        if l == n or nums[l] != target:
            return -1
        return l
                