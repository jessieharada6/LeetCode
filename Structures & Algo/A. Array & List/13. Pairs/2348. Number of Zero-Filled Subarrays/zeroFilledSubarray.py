class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans, l = 0, -1             # left起始-1 意义l在非0的位置
        for r, num in enumerate(nums):
            if num != 0:
                l = r
            else:
                ans += (r - l)
        
        return ans

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt, ans = 0, 0
        for num in nums:
            if num != 0:
                cnt = 0         # reset
            else:
                cnt += 1        # 累计0的个数
                ans += cnt
        
        return ans