class Solution:
    @lru_cache(None)
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        
        dp = [[False] * n for _ in range(n)]
        
        start = 0
        length = 0
        max_length = 1
        
        # for i in range(n):
        #     dp[i][i] = True
        
        for j in range(1, n):
            for i in range(j):          # no need to include j + 1, as j + 1 = i
                
                if s[i] == s[j]:
                    if j - i <= 2:
                        dp[i][j] = True
                        length = j - i + 1
                    
                    elif dp[i + 1][j - 1]:
                        dp[i][j] = True
                        length = j - i + 1
                    
                
                if dp[i][j]:
                    if max_length < length:
                        max_length = length
                        start = i
        
        # print(dp, start, length, max_length)
        return s[start : start + max_length]
