class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        map = {}
        # special case -[23,2,4,6,6] 7 => nums[1:3]   
        map[0] = -1
        runningSum = 0
        
        for i in range(len(nums)):
            runningSum += nums[i]

            if k != 0:
                runningSum %= k

            
            if runningSum in map:
                # must be 2 or more indexes
                if i - map[runningSum] >= 2:
                    return True
            else:
                map[runningSum] = i
        
        return False
            