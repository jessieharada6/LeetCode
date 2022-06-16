class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = 0

        def traverse(i, j):
            nonlocal temp
            if i < 0 or i >= m or j < 0 or j >= n:
                return          # return 0 if no arguments given in python, as temp is int type
            
            if grid[i][j] == 0:
                return
            
            grid[i][j] = 0
            temp += 1
            traverse(i + 1, j)
            traverse(i - 1, j)
            traverse(i, j + 1)
            traverse(i, j - 1)
            return temp
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    temp = 0
                    islands = max(islands, traverse(i, j))
        
        return islands