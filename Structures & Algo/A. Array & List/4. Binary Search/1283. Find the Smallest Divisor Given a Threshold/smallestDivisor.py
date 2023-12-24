class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def getSum(k):
            sum = 0
            for num in nums:
                sum += ceil(num / k)
            return sum
        
        l, r = 0 , int(10e6)
        while l + 1 < r:
            m = (l + r) // 2
            if getSum(m) <= threshold:
                r = m
            else:
                l = m
        
        return r

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # k is the divisor, threshold is the result 
        
        def getSum(k): 
            sum = 0
            for num in nums:
                sum += ceil(num / k)
            return sum
        
        l, r = 1, int(10e6)
        while l < r:
            m = l + (r - l) // 2
            if getSum(m) <= threshold:
                r = m
            else:
                l = m + 1
        
        return l