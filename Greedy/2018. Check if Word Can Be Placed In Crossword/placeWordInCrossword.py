class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        words = [word, word[::-1]]
        
        for row in board, zip(*board):
            for cell in row:
                each_row = ''.join(cell).split("#")
                for w in words:
                    for each_cell in each_row:
                        if len(each_cell) == n:
                            if all(each_cell[i] == " " or each_cell[i] == w[i] for i in range(n)):
                                return True
        return False

class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        words = [word, word[::-1]]
        
        #print(list(zip(*board)))
        
        #zip(*board) rotates 90 degrees 
        #1 2
        #3 4
        #becomes
        #3 1
        #2 4
        for row in board, zip(*board):
            #print(row, list(row))
            for cell in row:
                #print(cell, list(cell))
                #if #, it will become ''
                #if not, it will be whatevery it was used to be
                each_row = ''.join(cell).split("#")
                #print("q", each_row)
                for w in words:
                    # if no #, the cell should be combined
                    # thats what we are looking for
                    for each_cell in each_row:
                        if len(each_cell) == n:
                            #every element in the each_cell string must meet the condition IN ORDER
                            if all(each_cell[i] == w[i] or each_cell[i] == ' ' for i in range(n)):
                                return True
        return False