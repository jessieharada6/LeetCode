#  Time Complexity: O(m * n)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]
        
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        
        return len(word1) + len(word2) - dp[0][0] * 2
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        
        for i in range(1, m + 1):
            dp[0][i] += dp[0][i - 1] + 1
        
        for i in range(1, n + 1):
            dp[i][0] += dp[i - 1][0] + 1
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + 1

        return dp[-1][-1]
        
        
        #    "" s e a
        # "" 0  1 2 3
        # e  1  2 1 2
        # a  2  3 2 1  
        # t  3  4 3 2