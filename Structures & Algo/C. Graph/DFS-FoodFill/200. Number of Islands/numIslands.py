# foodfill
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
            
            # print(i, j)               # pre order
            traverse(i + 1, j)          # down
            traverse(i - 1, j)          # up
            traverse(i, j + 1)          # right
            traverse(i, j - 1)          # left
            
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    # print("outer", i, j)
                    islands += 1
                    traverse(i, j)          # water all adjencent lands, avoid repetition
        
        return islands


# visited version
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        def traverse(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            
            if grid[i][j] == "0" or visited[i][j]:       # if visted, return
                # visited[i][j] = True
                return
            
            # grid[i][j] = "0"                           # mark as visited
            visited[i][j] = True
            
            # print(i, j)
            traverse(i + 1, j)
            traverse(i - 1, j)
            traverse(i, j + 1)
            traverse(i, j - 1)
            
        
        for i in range(m):
            for j in range(n):
                # print(visited)
                if not visited[i][j] and grid[i][j] == "1":
                    # print("outer", i, j)
                    islands += 1
                    traverse(i, j)
        
        return islands