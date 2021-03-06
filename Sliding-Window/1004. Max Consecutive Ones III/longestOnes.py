class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        output = 0
        numT = numF = 0
        left = right = 0
        
        while right < len(nums):
            if nums[right] == 1:
                numT += 1
            else:
                numF += 1
            
            if numF > k:
                if nums[left] == 1:
                    numT -= 1
                else:
                    numF -= 1
                left += 1
            
            output = max(output, right - left + 1)
            right += 1
        
        return output


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = 0
        
        while right < len(nums):
            if nums[right] == 0:
                k -= 1
            
            if k < 0:
                # as the left pointer starts to move forward
                # increment k as we are sliding through
                if nums[left] == 0:
                    k += 1
                left += 1
            
            right += 1          
        
        return right - left