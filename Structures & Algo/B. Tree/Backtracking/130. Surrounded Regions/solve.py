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