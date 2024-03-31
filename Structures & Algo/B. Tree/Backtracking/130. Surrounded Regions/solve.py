class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        def dfs(i, j):
            # current executation
           if board[i][j] == "X": return
           if board[i][j] == "#": return
           board[i][j] = "#" 
           # end of current executation
           # next step
           for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= x < m and 0 <= y < n:
                    dfs(x, y)

        # def dfs(i, j):
        #     if i < 0 or i >= m or j < 0 or j >= n: return
            
        #     if board[i][j] == "X": return
        #     if board[i][j] == "#": return

        #     board[i][j] = "#"
        #     for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
        #         dfs(x, y)

        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    if board[i][j] == "O":
                        dfs(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "#":
                    board[i][j] = "O"
        


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return
            
            if board[row][col] == "X": 
                return # 不可以标记
            if board[row][col] == "#": 
                return # 已访问
                
            # 以上两个if条件保证了只有遇见O时 才标记#
            board[row][col] = "#"
            for r, c in (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1):
                # 因为当前board[row][col]是# 所以四方是O就会变# 是X就return即不变
                dfs(r, c)

        for i in range(len(board)):
            for j in range(len(board[0])):
                # 判断边边
                if i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1: 
                    if board[i][j] == "O":
                        dfs(i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O": # 先
                    board[i][j] = "X"
                if board[i][j] == "#": # 后
                    board[i][j] = "O"


# 不用从边边走
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        islands = 1
        # visited = [[False] * n for _ in range(m)]

        def dfs(row, col, islands):
            # print(row, col)
            if row < 0 or col < 0 or row >= m or col >= n:
                return
            
            if board[row][col] == "X":
                return

            if isinstance(board[row][col], int):
                return
            # if visited[row][col]:
            #     return

            # visited[row][col] = True
            board[row][col] = islands

            for r, c in (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1):
                dfs(r, c, islands)
        
        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == "O":
                    dfs(i, j, islands)
                    islands += 1

        edges = set()
        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] != "X" and (i == 0 or j == 0 or i == m - 1 or j == n - 1):
                    edges.add(board[i][j])

        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] not in edges:
                    board[i][j] = "X"
                if board[i][j] in edges:
                    board[i][j] = "O"


# 只用一次visited，保证o的地方只访问一次 
# 1. 用全局变量记录每个坐标
# 2. 用全局变量标识这一次所有的o有没有到达边界
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        #因为只访问o，每一个o只访问一次。所以不用生成新的visited.
        visited = [[False] * n for _ in range(m)] 

        def dfs(row, col):
            # print(row, col)
            if row < 0 or col < 0 or row >= m or col >= n:
                return
            
            if board[row][col] == "X":
                return

            if visited[row][col]:
                return

            visited[row][col] = True
            points.append([row, col])
            if row == 0 or col == 0 or row == m - 1 or col == n - 1:
                nonlocal touch
                touch = True

            for r, c in (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1):
                dfs(r, c)
        
        for i in range(0, m):
            for j in range(0, n):
                touch = False
                points = []
                if board[i][j] == "O":
                    dfs(i, j)
                    # print(touch, points)
                    if not touch:
                        for x, y in points:
                            board[x][y] = "X"