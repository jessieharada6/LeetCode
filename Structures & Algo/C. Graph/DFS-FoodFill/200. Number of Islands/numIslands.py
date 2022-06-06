class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        m = len(grid)
        n = len(grid[0])
        
        def traverse(i, j):
            nonlocal m
            nonlocal n
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            # print(i, j)           # pre order
            traverse(i + 1, j)      # down
            traverse(i - 1, j)      # up
            traverse(i, j + 1)      # right
            traverse(i, j - 1)      # left
            
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1
                    traverse(i, j)       # water all adjencent lands, avoid repetition
        
        return islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        m = len(grid)
        n = len(grid[0])
        
        def traverse(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            
            if grid[i][j] == "0":       # if visted, return
                return
            
            grid[i][j] = "0"            # mark as visited
            
            # print(i, j)
            traverse(i + 1, j)
            traverse(i - 1, j)
            traverse(i, j + 1)
            traverse(i, j - 1)
            
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    # print("outer", i, j)
                    islands += 1
                    traverse(i, j)
        
        return islands