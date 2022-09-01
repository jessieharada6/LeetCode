class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            triplets = self.threeSum(nums, i + 1, target - nums[i])
            
            for t in triplets:
                t.append(nums[i])
                res.append(t)
        
        return res
                
    
    def threeSum(self, nums, start, target):
        res = []
        n = len(nums)

        for i in range(start, n):
            if i > start and nums[i] == nums[i - 1]:
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
                