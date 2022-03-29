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