class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        m = nums[-1]
        for num in reversed(nums):
            k = (num - 1) // m
            ans += k
            m = num // (k + 1)
        
        return ans