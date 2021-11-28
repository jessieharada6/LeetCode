class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set) # key = c
        rows = collections.defaultdict(set) # key = r
        #print(dict(cols))
        squares = collections.defaultdict(set) # key = (r / 3, c / 3)
    
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] 
                or board[r][c] in cols[c]
                    # 9/2 = 4.5, 9//2 = 4
                or board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                
                # print("c", c, "R", r, "r//3", r//3, "c//3", c//3)
                # print(cols, rows, squares)
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        
        # print(cols, rows, squares)
                
        return True
                      
                

                    