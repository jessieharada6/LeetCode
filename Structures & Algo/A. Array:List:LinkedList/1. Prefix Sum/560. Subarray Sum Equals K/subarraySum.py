class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix sum base case
        preSum = {0: 1}
        current = 0
        res = 0
        
        for num in nums:
            # current prefix sum
            # hashMap records the prefix sum before the current num is added up
            current += num
            diff = current - k

            if diff in preSum:
                res += preSum[diff]
            
            # current hashMap
            preSum[current] = preSum.get(current, 0) + 1
        
        print(preSum)
        
        return res