class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        def is_attack(r, c, r1, c1):
            return c1 == c or c1 + r1 == c + r or c1 - r1 == c - r
        
        def dfs(cols):
            if len(cols) == n:
                print(cols)
                ans.append(["." * c + "Q" + "." * (n - c - 1) for c in cols])
                return
            
            for col in range(n):
                for r, c in enumerate(cols):
                    if is_attack(r, c, len(cols), col):
                        break
                else:
                    dfs(cols + [col])
        
        dfs([])
        return ans


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        def is_attack(r, c, r1, c1):
            return c1 == c or c1 + r1 == c + r or c1 - r1 == c - r
        
        def dfs(cols):
            if len(cols) == n:
                ans.append(["." * c + "Q" + "." * (n - c - 1) for c in cols])
                return
            
            for col in range(n):
                if not any(is_attack(r, c, len(cols), col) for r, c in enumerate(cols)):
                    dfs(cols + [col])
        
        dfs([])
        return ans

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