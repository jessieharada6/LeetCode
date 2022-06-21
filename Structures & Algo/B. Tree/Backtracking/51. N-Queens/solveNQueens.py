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