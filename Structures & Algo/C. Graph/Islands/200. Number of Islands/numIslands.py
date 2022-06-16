### grid[i][j] == "0" used as visited, to avoid repeatiion 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = 0
        
        def traverse(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            
            if grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            
            traverse(i + 1, j)
            traverse(i - 1, j)
            traverse(i, j + 1)
            traverse(i, j - 1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1
                    traverse(i, j)
        
        return islands
                
            
