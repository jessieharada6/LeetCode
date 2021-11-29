# preferred 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        output = -inf
        current_max = -inf
        
        for num in nums:
            # in each current_max
            # select num or num + current_max
            current_max = max(num, num + current_max)
            # use output to keep the final_max
            output = max(current_max, output)
        
        return output

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        output = nums[0]
        current_max = 0
        
        for num in nums:
            # accumulate
            # these two lines need to be together
            # if we output after resetting current_max to 0
            # then current_max is 0 not -1 e.g. [-1]
            current_max += num
            output = max(output, current_max)
            
            # if < 0, reset to 0
            if current_max < 0:
                current_max = 0
            
        return output
            
