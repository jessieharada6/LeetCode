class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        subs = 0

        def traverse(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            
            if grid2[i][j] == 0:
                return
            
            grid2[i][j] = 0
            traverse(i + 1, j)
            traverse(i - 1, j)
            traverse(i, j + 1)
            traverse(i, j - 1)
        
        for i in range(m):
            for j in range(n):
                # if grid1 is water, and grid2 is land, the land can't be the sub-island
                if grid1[i][j] == 0 and grid2[i][j] == 1:    # better than if grid1[i][j] != grid2[i][j], as it is easier to understand
                    traverse(i, j)
        # print(grid2)
        
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    subs += 1
                    traverse(i, j)
        
        return subs