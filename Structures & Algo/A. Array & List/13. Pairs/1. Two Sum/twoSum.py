class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for r, num in enumerate(nums):
            if target - num in d:
                return [d[target-num], r]
            d[num] = r


# pointers
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = sorted(zip(nums, range(len(nums))))
        
        l, r = 0, len(nums) - 1
        while l < r:
            s = d[l][0] + d[r][0]

            if s == target:
                return [d[l][1], d[r][1]]
            
            if s < target:
                l += 1
            else:
                r -= 1