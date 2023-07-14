class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        odd = 0
        even = nums[0]
        preOdd = odd
        preEven = even

        for i in range(1, n):
            odd = max(preOdd, preEven - nums[i])
            even = max(preEven, preOdd + nums[i])

            preOdd = odd
            preEven = even

        return max(odd, even)