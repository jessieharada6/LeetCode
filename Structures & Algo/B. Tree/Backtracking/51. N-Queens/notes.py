# ["".join(i) for i in board]:

# arr = []
# for p in path:
#     a = ''.join(p)
#     arr.append(a)


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # queens = [["." for _ in range(n)] for _ in range(n)]
        board = [['.'] * n for _ in range(n)]
        # print(["".join(i) for i in board])
        res = []
        
        def traverse(row):
            if row == n:
                q = ["".join(i) for i in board]    # 2d to 1d array
                res.append(q)
                return
            
            for col in range(n):
                if not isValid(row, col):
                    continue
                board[row][col] = "Q"
                traverse(row + 1)
                board[row][col] = "."
        
        def isValid(row, col):
            # check up
            for i in range(row):
                if board[i][col] == "Q":
                    return False
            
            # check up right
            for i, j in zip(range(row - 1, -1, -1), range(col + 1, n, 1)):
                if board[i][j] == "Q":
                    return False  
            
            # check up left
            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if board[i][j] == "Q":
                    return False  
            
            return True
        
        
        traverse(0)
        return res


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # queens = [["." for _ in range(n)] for _ in range(n)]
        board = [['.'] * n for _ in range(n)]
        # print(["".join(i) for i in board])
        res = []
        
        def traverse(row):
            if row == n:
                q = ["".join(i) for i in board]    # 2d to 1d array
                res.append(q)
                return
            
            for col in range(n):
                if not isValid(row, col):
                    continue
                board[row][col] = "Q"
                traverse(row + 1)
                board[row][col] = "."
        
        def isValid(row, col):
            # print("row", row, "col", col)
            # check up
            for i in range(row - 1, -1, -1):
                # print("i", i)
                if board[i][col] == "Q":
                    return False
            
            # check up right
            for i, j in zip(range(row - 1, -1, -1), range(col + 1, n, 1)):
                # print("right", "i", i, "j", j)
                if board[i][j] == "Q":
                    return False  
            
            # check up left
            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                # print("left", "i", i, "j", j)
                if board[i][j] == "Q":
                    return False  
            
            return True
        
        traverse(0)
        return res