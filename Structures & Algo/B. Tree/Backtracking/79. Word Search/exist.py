class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, idx):
            if idx == len(word):
                return True
            
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return False
            
            if word[idx] != board[row][col]:
                return False
            
            board[row][col] = "#"
            for r, c in (row, col + 1), (row + 1, col), (row, col -1), (row -1, col):
                if dfs(r, c, idx + 1):
                    return True
            board[row][col] = word[idx]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        
        return False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, idx):
            if idx == len(word):
                return True
            
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return False
            
            if word[idx] != board[row][col]:
                return False
            
            board[row][col] = "#"
            for rOffset, cOffset in (0, 1), (1, 0), (0, -1), (-1, 0):
                if dfs(row + rOffset, col + cOffset, idx + 1):
                    return True
            board[row][col] = word[idx]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        
        return False