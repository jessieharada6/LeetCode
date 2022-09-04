class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        target = 0

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            pairs = self.twoSum(nums, i + 1, target - nums[i])

            for p in pairs:
                p.append(nums[i])
                res.append(p)

        return res
    
    def twoSum(self, nums, start, target):
        res = []
        lo = start
        hi = len(nums) - 1

        while lo < hi:
            l = nums[lo]
            r = nums[hi]
            s = l + r
            if s < target:
                while lo < hi and l == nums[lo]: lo += 1
            elif s > target:
                while lo < hi and r == nums[hi]: hi -= 1
            else:
                res.append([l, r])
                while lo < hi and l == nums[lo]: lo += 1
                while lo < hi and r == nums[hi]: hi -= 1
        return res