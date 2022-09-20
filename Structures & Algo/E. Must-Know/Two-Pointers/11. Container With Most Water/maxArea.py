class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        max_area = 0
        l, r = 0, len(height) - 1
        
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            max_area = max(area, max_area)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
        return max_area

# overdoes
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        max_area = 0
        l_max, r_max = height[0], height[-1]
        l, r = 0, len(height) - 1
        
        while l < r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])
            
            
            if l_max < r_max:
                area = l_max * (r - l)
                l += 1
            else:
                area = r_max * (r - l)
                r -= 1
            
            max_area = max(area, max_area)
        
        return max_area