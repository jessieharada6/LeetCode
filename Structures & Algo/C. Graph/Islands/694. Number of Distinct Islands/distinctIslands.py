class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = 0
        serialisedPatterns = defaultdict(int)
        
        
        def traverse(i, j, arr, dirs):
            if i < 0 or i >= m or j < 0 or j >= n:
                return

            if grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            
            arr.append(dirs)
            traverse(i + 1, j, arr, 1)
            traverse(i - 1, j, arr, 2)
            traverse(i, j + 1, arr, 3)
            traverse(i, j - 1, arr, 4)
            arr.append(-dirs)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1
                    arr = []
                    traverse(i, j, arr, 666)
                    # record the traversal order to get the pattern
                    serialisedPatterns[",".join(str(x) for x in arr)] += 1
                    
        print(serialisedPatterns)
        return len(serialisedPatterns)



# defaultdict(<class 'int'>, {'666,3,3,-3,-3,-666': 0, '666,-666': 0, '666,3,-3,-666': 0})
# [["1","1","1","0","0"],["0","0","0","1","0"],["1","1","0","0","0"],["0","0","1","1","1"]]
            