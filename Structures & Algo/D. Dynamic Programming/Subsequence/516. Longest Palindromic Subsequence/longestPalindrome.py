class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
        
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        return dp[0][n - 1]

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        memo = [[0] * n for _ in range(n)]
        
        def dp(i, j):
            if i < 0 or j < 0 or i >= n or j >= n or i > j:
                return 0
            
            if i == j:
                return 1
            
            if memo[i][j]:
                return memo[i][j]
            
            if s[i] == s[j]:
                memo[i][j] = dp(i + 1, j - 1) + 2
            else:
                memo[i][j] = max(dp(i + 1, j), dp(i, j - 1))
            
            return memo[i][j]
        
        return dp(0, n - 1)