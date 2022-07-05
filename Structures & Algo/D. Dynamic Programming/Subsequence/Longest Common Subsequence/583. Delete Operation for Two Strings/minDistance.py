class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        lcs = self.longestCommonSubsequence(word1, word2)
        
        return len(word1) + len(word2) - lcs * 2
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1) 
        n = len(text2)
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1) 
        n = len(word2)
        
        dp = [0] * (n + 1) 

        for i in range(1, m + 1):
            base = 0
            for j in range(1, n + 1):
                prev = dp[j]
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = base + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                base = prev
        
        return m + n - dp[-1] * 2
        
        