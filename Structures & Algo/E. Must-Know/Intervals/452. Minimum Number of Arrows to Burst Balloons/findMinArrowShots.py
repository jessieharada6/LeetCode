class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])
        n = len(points)
        o = 0
        prev = points[0]
        
        for i in range(1, n):
            curr = points[i]
            if prev[1] >= curr[0]:
                o += 1
            else:
                prev[1] = curr[1]
        
        return n - o