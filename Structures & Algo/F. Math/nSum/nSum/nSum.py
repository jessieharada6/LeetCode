class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.nSum(nums, 4, 0, target)
    
    def nSum(self, nums, n, start, target):
        res = []
        if n < 2 or len(nums) < n: return res
        
        if n == 2:
            res = self.twoSum(nums, start, target)
        else:
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                sub = self.nSum(nums, n - 1, i + 1, target - nums[i])

                for s in sub:
                    s.append(nums[i])
                    res.append(s)

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
                