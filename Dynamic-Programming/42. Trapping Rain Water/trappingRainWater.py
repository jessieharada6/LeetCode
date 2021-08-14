class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # for case of [], to avoid runtime error
        if n == 0:
            return 0
        
        water = 0
        l = 0 
        r = n - 1 
        max_l = height[0]
        max_r = height[n - 1]
        
        while l < r:
            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                water += (max_l - height[l])
            else:
                r -= 1
                max_r = max(max_r, height[r])
                water += (max_r - height[r])
        
        return water