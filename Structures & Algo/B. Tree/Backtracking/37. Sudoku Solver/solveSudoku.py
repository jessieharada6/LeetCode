class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        n = 9
        
        def traverse(i, j):
            if i == n: 
                return True
            
            if j == n:
                return traverse(i + 1, 0)
            
            if board[i][j] != ".":
                return traverse(i, j + 1)
            
            for k in range(1, n + 1):
                char = str(k)
                if not isValid(i, j, char): continue
                
                board[i][j] = char
                if traverse(i, j + 1): return True
                board[i][j] = "."
            
            return False
        
        def isValid(r, c, char):
            for i in range(n):
                if board[r][i] == char: return False # horizontal line
                if board[i][c] == char: return False # vertical line
                if board[(r // 3) * 3 + (i // 3)][(c // 3) * 3 + (i % 3)] == char: return False
            return True
        
        traverse(0, 0)
        

