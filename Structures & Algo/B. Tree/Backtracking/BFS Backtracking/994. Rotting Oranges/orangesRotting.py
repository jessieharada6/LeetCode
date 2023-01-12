class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        depth = -1
        cur = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    cur.append((i, j))
        
        while cur:
            nxt = []
            for x, y in cur:
                if 0 <= x + 1 < len(grid) and grid[x + 1][y] == 1: 
                    nxt.append((x + 1, y))
                    grid[x + 1][y] = 2
                if 0 <= x - 1 <= len(grid) and grid[x - 1][y] == 1: 
                    nxt.append((x - 1, y))
                    grid[x - 1][y] = 2
                if 0 <= y + 1 < len(grid[0]) and grid[x][y + 1] == 1: 
                    nxt.append((x, y + 1))
                    grid[x][y + 1] = 2
                if 0 <= y - 1 <= len(grid[0]) and grid[x][y - 1] == 1: 
                    nxt.append((x, y - 1))
                    grid[x][y - 1] = 2
            # print(cur, nxt)
            cur = nxt
            depth += 1
        # print(depth, grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return depth if depth != -1 else 0