class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # a + b > c
        
        nums.sort()
        ans = 0
        
        for i in range(2, len(nums)):
            j = i - 1    #向左探寻 找到边界 
            k = 0        #向右探寻 让当前s增大
            
            if nums[i - 1] + nums[i - 2] < nums[i]:
                continue
            
            while k < j:
                s = nums[j] + nums[k]
                if s > nums[i]:
                    ans += j - k
                    j -= 1
                else:
                    k += 1
        
        return ans