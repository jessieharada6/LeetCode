# simplified version
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchBoundary(l, r, left_biased):
            i = -1
            while l <= r:
                m = floor(l + (r - l) / 2)
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                elif nums[m] == target:
                    i = m
                    
                    if left_biased:
                        r = m - 1
                    else:
                        l = m + 1
                
            return i
        
        left = searchBoundary(0, len(nums) - 1, True)
        right = searchBoundary(0, len(nums) - 1, False)
        return [left, right]

# elaborated version
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchLeftPosition(l, r):
            while l <= r:
                m = floor(l + (r - l) / 2)
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                elif nums[m] == target:
                    # let r minimise the range
                    # leave loop when l == r + 1
                    r = m - 1
                
            # if target is larger than any num
            if l == len(nums) or nums[l] != target:
                return -1
            # l is the returning point
            return l
        
        def searchRightPosition(l, r):
            while l <= r:
                m = floor(l + (r - l) / 2)
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                elif nums[m] == target:
                    # let l minimise the range
                    # leave loop when l == r + 1
                    l = m + 1
                    
            # if target is smaller than any num 
            if r == -1 or nums[r] != target:
                return -1
            # r is the returning point
            return r

        left = searchLeftPosition(0, len(nums) - 1)
        right = searchRightPosition(0, len(nums) - 1)
        return [left, right]