class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # multiples of zero can be any number 
        # [5,0,0,0]
        # 3 - true
        
        # [23,2,4,6,6]
        # 7
        # need map[0] = -1
        # at the 4th index, remainder is 0 which meets the conditions
        
        running_sum = 0
        map = {}
        map[0] = -1
        
        for i in range(len(nums)):
            running_sum += nums[i]
            if k != 0:
                running_sum %= k
            
            if running_sum in map:
                if i - map[running_sum] >= 2:
                    return True
            else:
                map[running_sum] = i
        
        return False