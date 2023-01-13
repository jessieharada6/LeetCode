class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific_queue = []
        atlantic_queue = []
        visited_pacific = [[False] * n for _ in range(m)]
        visited_atlantic = [[False] * n for _ in range(m)]

        def bfs(cur, visited):
            while cur:
                nxt = []
                for x, y in cur:
                    for r, c in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                        if r < 0 or c < 0 or r >= m or c >= n or visited[r][c] or heights[r][c] < heights[x][y]:
                            continue
                        visited[r][c] = True
                        nxt.append((r, c))
                cur = nxt
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    pacific_queue.append((i, j))
                    visited_pacific[i][j] = True
                    bfs(pacific_queue, visited_pacific)
                if i == m - 1 or j == n - 1:
                    atlantic_queue.append((i, j))
                    visited_atlantic[i][j] = True
                    bfs(atlantic_queue, visited_atlantic)
        
        ans = []
        for i in range(m):
            for j in range(n):
                if visited_pacific[i][j] and visited_atlantic[i][j]:
                    ans.append([i, j])
        
        return ans

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        
        visited_pacific = [[False] * n for _ in range(m)]
        visited_atlantic = [[False] * n for _ in range(m)]

        def dfs(visited, cur, row, col):
            if row < 0 or col < 0 or row >= m or col >= n or visited[row][col] or heights[row][col] < cur:
                return
            
            visited[row][col] = True
            for r, c in (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1):
                dfs(visited, heights[row][col], r, c)

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dfs(visited_pacific, -math.inf, i, j)
                if i == m - 1 or j == n - 1:
                    dfs(visited_atlantic, -math.inf, i, j)
        
        ans = []
        for i in range(m):
            for j in range(n):
                if visited_pacific[i][j] and visited_atlantic[i][j]:
                    ans.append([i, j])
        
        return ans