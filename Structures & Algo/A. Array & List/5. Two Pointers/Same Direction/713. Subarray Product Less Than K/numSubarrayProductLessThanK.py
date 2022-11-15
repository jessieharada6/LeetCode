
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:        # strictly less than k [1,1,1,1] k = 1
            return 0
        
        m = 1
        ans = 0
        l = 0
        
        for r, num in enumerate(nums):
            m *= num
            
            # 进来前false
            while m >= k:
                m //= nums[l]
                l += 1
            # 出来后true
            
            # 现在已经m < k了
            ans += (r - l + 1)
        
        return ans

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