class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        nMap = {}
        
        nMap[0] = -1
        nSum = 0
        output = 0
        
        for i in range(len(nums)):
            nSum += nums[i] if nums[i] == 1 else -1

            if nSum in nMap:
                output = max(output, i - nMap[nSum])
            else:
                nMap[nSum] = i
            
        return output