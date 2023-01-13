class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []
        m, n = len(heights), len(heights[0])
        pacific = []
        atlantic = []
        valid_pacific = [[False] * n for _ in range(m)]
        valid_atlantic = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    valid_pacific[i][j] = True
                    pacific.append((i, j))
                if i == m - 1 or j == n - 1:
                    valid_atlantic[i][j] = True
                    atlantic.append((i, j))
        
        def bfs(ocean, visited):
            while ocean:
                nxt = []
                for x, y in ocean:
                    for r, c, in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                        if r < 0 or c < 0 or r >= m or c >= n or visited[r][c] or heights[r][c] < heights[x][y]:
                            continue
                        visited[r][c] = True
                        nxt.append((r,c))
                ocean = nxt

        bfs(pacific, valid_pacific)
        bfs(atlantic, valid_atlantic)

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if valid_pacific[i][j] and valid_atlantic[i][j]:
                    ans.append([i, j])

        return ans

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []
        m, n = len(heights), len(heights[0])
        pacific = []
        atlantic = []
        valid_pacific = [[False] * n for _ in range(m)]
        valid_atlantic = [[False] * n for _ in range(m)]

        def dfs(ocean, visited, cur, row, col):
            if row < 0 or col < 0 or row >= m or col >= n or visited[row][col] or heights[row][col] < cur:
                return
            
            visited[row][col] = True
            for r, c in (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1):
                dfs(ocean, visited, heights[row][col], r, c)

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dfs(pacific, valid_pacific, -math.inf, i, j)
                if i == m - 1 or j == n - 1:
                    dfs(atlantic, valid_atlantic, -math.inf, i, j)
        
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if valid_pacific[i][j] and valid_atlantic[i][j]:
                    ans.append([i, j])

        return ans