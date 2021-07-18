class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) < 3:
            return result
        
        # sort
        nums.sort()
        
        # for index, value in enumerate(arr)
        for i, num in enumerate(nums):
            if num > 0: 
                break
            if i > 0 and num == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                sum = num + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                if sum < 0:
                    l += 1
                if sum == 0:
                    result.append([num, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                    
        return result
            