class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])  
        
        cnt, ans = 0, 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    if 0 <= i - 1 < m and grid[i - 1][j] == 1:
                        cnt += 1
                    if 0 <= i + 1 < m and grid[i + 1][j] == 1:
                        cnt += 1
                    if 0 <= j - 1 < n and grid[i][j - 1] == 1:
                        cnt += 1
                    if 0 <= j + 1 < n and grid[i][j + 1] == 1:
                        cnt += 1
                    ans += 4 - cnt
                    cnt = 0

        return ans 