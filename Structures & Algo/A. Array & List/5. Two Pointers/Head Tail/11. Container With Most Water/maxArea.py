class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 固定更短边 此时 无论另一边如何相向移动 都不可能找到比当前更大的面积了
        # 所以当前更短边没有用了 pointer可以移动了
        
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            ans = max(ans, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return ans
            