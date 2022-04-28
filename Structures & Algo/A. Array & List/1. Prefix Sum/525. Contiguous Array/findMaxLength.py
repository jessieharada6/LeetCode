class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # base case - as index starts from 0
        prefix = {0: -1}
        sum = 0
        output = 0
        
        for i in range(len(nums)):
            sum += nums[i] if nums[i] != 0 else -1

            if sum in prefix:
                output = max(output, i - prefix[sum])
            else:
                prefix[sum] = i
        
        return output

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        s = {0: -1}
        sum = 0
        ans = 0
        
        for i in range(len(nums)):
            sum += -1 if nums[i] == 0 else nums[i]
            
            if sum in s:
                ans = max(ans, i - s[sum])
            
            if sum not in s:
                s[sum] = i
        
        return ans