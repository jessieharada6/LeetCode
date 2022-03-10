class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        output = 0
        
        # base case: sum is 0 as prefix sum
        even = 1
        odd = 0
        mod = 10 ** 9 + 7
        sum = 0
        
        for n in arr:
            sum += n
            
            if sum & 1:
                odd += 1
                output += even # odd + even = odd
            else:
                even += 1
                output += odd # even + odd = odd
        
        return output % mod