class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 0
        l = _or = 0
        for r, num in enumerate(nums):
            while _or & num:
                _or ^= nums[l]
                l += 1
            _or |= num
            res = max(res, r - l + 1)

        return res