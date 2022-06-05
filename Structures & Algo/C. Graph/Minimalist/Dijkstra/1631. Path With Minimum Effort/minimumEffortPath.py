
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        
        heap = []
        heapq.heappush(heap, (0, 0, 0)) # min effort -> min heap
        
        visited = [[False] * m for _ in range(n)]
        dist = [[math.inf] * m for _ in range(n)]
        
        while heap:
            effort, y, x = heapq.heappop(heap)
            # print("y", y, "x", x)
            if visited[y][x]:
                continue
                
            visited[y][x] = True
            dist[y][x] = effort
            
            for dy, dx in directions:
                yy = y + dy
                xx = x + dx
                # print(yy, xx)
                
                if yy < 0 or yy >= n or xx < 0 or xx >= m or visited[yy][xx]:
                    continue
                
                # effort = max abs (current node val - up/down/l/r node val)
                # push the min effort
                heapq.heappush(heap,(max(effort, abs(heights[y][x] - heights[yy][xx])), yy, xx))    
                # print(dist)
        
        return dist[n - 1][m - 1]