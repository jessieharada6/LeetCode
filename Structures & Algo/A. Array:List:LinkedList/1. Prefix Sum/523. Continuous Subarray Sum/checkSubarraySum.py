class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # if sum(nums[i:j]) % k == 0 and i < j
        # then sum(nums[:i]) % k = sum(nums[:j] % k) 
        # (not include i) but (include j) >= 2
        
        sum = 0
        # base case 
        # for example [1, 1] k = 2 
        # mod is 0
        record = {0: -1}
        
        for i in range(len(nums)):
            sum += nums[i]
            sum %= k
            
            if sum in record:
                if i - record[sum] >= 2:
                    return True
            else:
                record[sum] = i
        
        return False