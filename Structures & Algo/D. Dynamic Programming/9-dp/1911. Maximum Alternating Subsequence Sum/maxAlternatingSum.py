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

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)

        odd, even = 0, 0
        # if nums has negative int
        preOdd, preEven = -inf, 0 # len(0) 长度不是sum 
        
        for x in nums:
            odd = max(preOdd, preEven + x)
            even = max(preEven, preOdd - x)

            preOdd = odd
            preEven = even
        return max(odd, even)
# print(Solution().maxAlternatingSum([-2,-2,-2,-2])) <-- check first case - stdout