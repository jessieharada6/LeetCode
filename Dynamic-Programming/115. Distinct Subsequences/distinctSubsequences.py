class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        
        # same length and string      
        if m == n and s == t:
            return 1
        # s as the longer string, 
        # length should not be less than t       
        if m < n:
            return 0;
        
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        
        # fill in base case - first row
        for i in range(m + 1):
            dp[0][i] = 1
        
        # now looking at each string
        for i in range(n):
            for j in range(m):
                if t[i] == s[j]:
                    dp[i + 1][j + 1] = dp[i][j] + dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j]
        
        return dp[-1][-1]