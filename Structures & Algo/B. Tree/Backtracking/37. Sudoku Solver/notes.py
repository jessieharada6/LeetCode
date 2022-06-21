class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        n = 9
        
        def traverse(i, j):
            if i == n:                                # base case
                return True                           # found solution
            
            if j == n:                                # horizontal line finished
                return traverse(i + 1, 0)             # new line, starting from 0 
            
            if board[i][j] != ".":                    # has number
                return traverse(i, j + 1)             # move to the next element
               
            for k in range(1, 10):
                if not isValid(i, j, str(k)): 
                    continue
                board[i][j] = str(k)
                if traverse(i, j + 1): return True   # move to the next element 
                board[i][j] = "."
            
            return False

        
        def isValid(row, col, char): 
            for i in range(9):
                if board[row][i] == char: return False
                if board[i][col] == char: return False
                if board[(row // 3) * 3 + (i // 3)][(col // 3) * 3 + i % 3] == char: return False
            return True
        
        traverse(0,0)

def isValid(row,col,val):
    #判断行里是否重复
    for i in range(9):  
        if board[row][i] == val:
            return False

    #判断列里是否重复
    for j in range(9):  
        if board[j][col] == val:
            return False
    
    #判断9方格里是否重复
    startRow = (row // 3) * 3
    startcol = (col // 3) * 3
    for i in range(startRow,startRow + 3):  
        for j in range(startcol,startcol + 3):
            if board[i][j] == val:
                return False
    return True