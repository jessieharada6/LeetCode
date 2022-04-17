class Solution:
    def minInsertions(self, s: str) -> int:
        # legit - ())

        res = 0     # amount of insertions needed - ** when i look back
        right = 0   # amount of right brackets needed - should always be even not odd - ** when i look from left to right 
        
        for b in s:
            if b == "(":
                right += 2
                if right % 2 == 1: # (()))( 
                    res += 1       # (())))(
                    right -= 1 # as need of insertions increase by 1, reduce 1 to balance out
            else:
                if b == ")":
                    right -= 1 
                    if right == -1: # ) 
                        right = 1   # ))
                        res += 1    # ())

        return res + right
    
