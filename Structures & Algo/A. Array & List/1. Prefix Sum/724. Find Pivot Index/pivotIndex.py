class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lPrefix = []
        rPrefix = []
        
        sum = 0    
        for i in range(len(nums)):
            sum += nums[i]
            lPrefix.append(sum)
        
        sum = 0    
        for i in range(len(nums) - 1, -1, -1):
            sum += nums[i]
            rPrefix.append(sum)
        
        # print(lPrefix, rPrefix)
        
        for i in range(len(lPrefix)):
            if lPrefix[i] == rPrefix[len(rPrefix) - 1 - i]:
                return i
            
        return -1
                

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l, r = 0, sum(nums)
        
        for index, num in enumerate(nums):
            r -= num  
            if r == l:
                return index
            # let l be one index late
            l += num
            
        return -1

        