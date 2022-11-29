class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        l, r = 0, n - 1
        
        while l <= r:
            m = (l + r) // 2
            isTrue = self.canReach(m, heights, bricks, ladders)
            if isTrue:
                l = m + 1
            else:
                r = m - 1
        
        return r
    
    def canReach(self, m, heights, bricks, ladders):
        diff = []
        for i in range(m):
            if heights[i] < heights[i + 1]:
                diff.append(heights[i + 1] - heights[i])
        
        n = len(diff)
        if n <= ladders:
            return True
        
        diff.sort(reverse=True)
        s = 0
        for i in range(ladders , n):
            s += diff[i]
            
        return s <= bricks


class Solution: 
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        l, r = 0, n - 1

        while l <= r:
            m = (l + r) // 2
            isTrue = self.canReach(m, heights, bricks, ladders)
            if isTrue:
                l = m + 1
            else:
                r = m - 1
        return r
    
    def canReach(self, m, heights, bricks, ladders):
        diff = []
        for i in range(m):
            if heights[i] < heights[i + 1]:
                diff.append(heights[i + 1] - heights[i])
        diff.sort(reverse=True)
        count = 0
        for d in diff:
            if ladders - 1 >= 0:
                ladders -= 1
            elif bricks - d >= 0:
                bricks -= d
            else:
                break
            count += 1
        if count == len(diff):
            return True
        else:
            return False