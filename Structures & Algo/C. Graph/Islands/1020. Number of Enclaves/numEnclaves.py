class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        moves = 0
        
        def traverse(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            
            if grid[i][j] == 0:
                return
            
            grid[i][j] = 0
            traverse(i - 1, j)
            traverse(i + 1, j)
            traverse(i, j - 1)
            traverse(i, j + 1)
        
        # mark edges as 0
        for i in range(m):
            traverse(i, 0)
            traverse(i, n - 1)
        
        for j in range(n):
            traverse(0, j)              # if grid[0][j] == 1: 
            traverse(m - 1, j)
        
        # calculate enclaves 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    moves += 1
        
        return moves