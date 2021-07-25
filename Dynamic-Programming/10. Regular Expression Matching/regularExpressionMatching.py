class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(2, len(p) + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]
       
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] in {s[i - 1], "."}:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    # 0 preceding element                
                    if dp[i][j - 2] == True:
                        dp[i][j] = True
                    # 1 preceding element 
                    elif p[j - 2] in {s[i - 1], "."}:
                        dp[i][j] = dp[i - 1][j]
        
        return dp[-1][-1]