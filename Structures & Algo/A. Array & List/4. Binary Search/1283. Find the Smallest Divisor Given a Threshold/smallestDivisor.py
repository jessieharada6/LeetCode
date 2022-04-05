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