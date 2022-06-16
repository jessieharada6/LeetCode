class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = 0

        def traverse(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            
            if grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0

            # same as temp += 1
            return traverse(i + 1, j) + traverse(i - 1, j) + traverse(i, j + 1) + traverse(i, j - 1) + 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    islands = max(islands, traverse(i, j))
        
        return islands