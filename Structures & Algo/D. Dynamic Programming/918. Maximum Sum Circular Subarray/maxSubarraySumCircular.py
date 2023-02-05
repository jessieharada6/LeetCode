class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        
        most, _, b = nums[0], nums[0], nums[0]
        for i in range(1, n):
            _, b = b, max(nums[i] + b, nums[i])
            most = max(most, b)
        
        least, _, b = nums[0], nums[0], nums[0]
        for i in range(1, n):
            _, b = b, min(nums[i] + b, nums[i])
            least = min(least, b)
        
        # print(least, most)
        return max(sum(nums) - least if sum(nums) != least else -math.inf, most)