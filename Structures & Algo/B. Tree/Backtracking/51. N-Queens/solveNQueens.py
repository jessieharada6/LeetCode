class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        path = [['.'] * n for _ in range(n)]
        def dfs(i):
            if i == n:
                ans.append([''.join(p) for p in path])
                return
            
            for j in range(n):
                if isValid(i, j):
                    path[i][j] = "Q"
                    dfs(i + 1)
                    path[i][j] = "."
        
        def isValid(row, col):
            # up
            for i in range(row - 1, -1, -1):
                if path[i][col] == "Q":
                    return False

            # left
            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if path[i][j] == "Q":
                    return False
            
            # right
            for i, j in zip(range(row - 1, -1, -1), range(col + 1, n, 1)):
                if path[i][j] == "Q":
                    return False
            return True
            
        print([['.'] * n for _ in range(n)])
        dfs(0)
        return ans



class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        boards = []
        
        def traverse(row):                      # go by depth
            if row == n:
                boards.append(["".join(b) for b in board])
                return
            
            for col in range(n):                # explore breadth                
                if not isValid(board, row, col): continue

                board[row][col] = "Q"
                traverse(row + 1)
                board[row][col] = "."
        
        def isValid(board, row, col):
            # up
            for i in range(row):
                if board[i][col] == "Q":
                    return False
            
            # up left
            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if board[i][j] == "Q":
                    return False
            
            #up right
            for i, j in zip(range(row - 1, -1, -1), range(col + 1, n, 1)):
                if board[i][j] == "Q":
                    return False
            
            return True
        
        traverse(0)
        return boards