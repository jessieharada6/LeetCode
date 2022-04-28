class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = {0 : 1}                     # use map to record the number of the sum
        sum = 0
        ans = 0
        
        for n in nums:
            sum += n
            
            if sum - k in s:
                ans += s[sum - k]
            
            s[sum] = s.get(sum, 0) + 1
        
        return ans
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