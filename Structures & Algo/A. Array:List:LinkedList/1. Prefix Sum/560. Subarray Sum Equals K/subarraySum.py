class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix sum base case: an element itself is k
        prefix = {0: 1}
        sum = 0
        output = 0
        
        for num in nums:
            # current prefix sum
            # hashMap records the prefix sum before the current num is added up
            sum += num
            
            if sum - k in prefix:
                output += prefix[sum - k]
            
            # current hashMap
            prefix[sum] = prefix.get(sum, 0) + 1
        
        # print(preSum)
        
        return res