class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # psum
        # < k  ： r移动
        # >= k ： l移动 并 减去nums[l]
        
        s, l ,ans = 0, 0, inf
        for r, x in enumerate(nums):
            s += x
            while s >= target:
                ans = min(ans, r - l + 1)
                s -= nums[l]
                l += 1
                
        return ans if ans != inf else 0