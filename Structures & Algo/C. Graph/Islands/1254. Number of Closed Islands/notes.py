class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = 0
        
        def traverse(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            
            if grid[i][j] == 1:
                return
            
            grid[i][j] = 1
            traverse(i + 1, j)
            traverse(i - 1, j)
            traverse(i, j + 1)
            traverse(i, j - 1)
        
        # make 0s to 1s for edges 
        for i in range(m):
            if grid[i][0] == 0:         #  not required, as traverse() will check
                traverse(i, 0)
            if grid[i][n - 1] == 0:     #  not required, as traverse() will check
                traverse(i, n - 1)
        
        for j in range(n):
            if grid[0][j] == 0:         #  not required, as traverse() will check
                traverse(0, j)
            if grid[m - 1][j] == 0:     #  not required, as traverse() will check
                traverse(m - 1, j)
        
        # calculate closed islands - same as number of islands
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    islands += 1
                    traverse(i, j)
        
        return islands
            
            