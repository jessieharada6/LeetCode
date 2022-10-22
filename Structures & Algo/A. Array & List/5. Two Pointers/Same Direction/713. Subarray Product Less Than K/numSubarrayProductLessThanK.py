class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # psum -> pproduct
        # < k  ： r移动
        # >= k ： l移动 并 除掉nums[l]
        
        l = ans = 0
        p = 1
        for r, x in enumerate(nums):
            p *= x
            while p >= k and l < len(nums):
                p = p // nums[l]
                l += 1
            
            if p < k:   # 加这个限制 在外圈走的时候不会被误加
                ans += (r - l + 1)
        
        return ans