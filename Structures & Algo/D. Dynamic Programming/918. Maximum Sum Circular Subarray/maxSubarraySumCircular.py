class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 非空最大子数组和
        most, b = nums[0], nums[0]
        for i in range(1, n):
            b = max(nums[i] + b, nums[i])
            most = max(most, b)
        
        # 非空最小子数组和
        least, b = nums[0], nums[0]
        for i in range(1, n):
            b = min(nums[i] + b, nums[i])
            least = min(least, b)
        
        # 非空最小子数组和有可能会是全部-当所有数为负数 - sum(nums) != least
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