class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left, right = 0, 0
        ans = 0
        
        while l < r:
            left = max(left, height[l])
            right = max(right, height[r])
            
            if left < right:
                ans += left - height[l]
                l += 1
            else:
                ans += right - height[r]
                r -= 1
                
        
        return ans

class Solution:
    def trap(self, height: List[int]) -> int:
        # 不需要完全知道左右边的高度 
        # 只需要知道更短边即可 - 取决于短板
        
        l, r = 0, len(height) - 1
        # 事先算出左右边的高度 
        left, right = height[l], height[r]
        ans = 0
        
        while l < r:
            if left < right:
                ans += left - height[l]
                l += 1
                # 更新高度
                left = max(left, height[l])
            else:
                ans += right - height[r]
                r -= 1
                # 更新高度 
                right = max(right, height[r])
        
        return ans