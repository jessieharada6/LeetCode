class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 非空最大子数组和：1.中间的那段最大
        most, b = -math.inf, -math.inf
        for x in nums:
            b = max(x + b, x)
            most = max(most, b)
        
        # 非空最小子数组和：2.两头的那段最大 - 算出中间那段最小的值
        least, b = math.inf, math.inf
        for x in nums:
            b = min(x + b, x)
            least = min(least, b)
        
        # 非空最小子数组和有可能会是全部
        # 当所有数为负数： sum(nums) != least 这样得出的子集是空子集不符合题意
        return max(sum(nums) - least if sum(nums) != least else -math.inf, most)

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        most, b = -math.inf, -math.inf
        for x in nums:
            b = max(x + b, x)
            most = max(most, b)
        
        least, b = math.inf, math.inf
        for x in nums:
            b = min(x + b, x)
            least = min(least, b)
        
        return max(sum(nums) - least if sum(nums) != least else -math.inf, most)