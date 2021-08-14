class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1) + 1
        m = len(word2) + 1
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] + 1
        
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + 1
            
        for i in range(1, m):
            for j in range(1, n):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
                
        return dp[-1][-1]