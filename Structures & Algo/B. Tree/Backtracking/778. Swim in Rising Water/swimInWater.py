class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        temp = grid[0][0]

        def dfs(visited, cur, row, col, t):
            if row < 0 or row >= n or col < 0 or col >= n or visited[row][col] or cur != max(t, grid[row][col]):
                return
            
            visited[row][col] = True
            for r, c in (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1):
                dfs(visited, grid[0][0], r, c, t)

        def can_reach(t):
            grid[0][0] = max(t, temp)
            visited = [[False] * n for _ in range(n)]
            dfs(visited, grid[0][0], 0, 0, t)
            return visited[-1][-1]

        l = 0
        r = -1
        for i in range(n):
            for j in range(n):
                if grid[i][j] > r:
                    r = grid[i][j]

        while l <= r:
            m = (l + r) // 2
            if can_reach(m):
                r = m - 1
            else:
                l = m + 1
        
        return l