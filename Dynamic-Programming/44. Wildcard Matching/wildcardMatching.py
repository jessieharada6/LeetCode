class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]
        
        # [0][0] is "" vs ""
        dp[0][0] = True
        # for the first row, set values to true until we see the first non-* character
        for j in range(1, len(p) + 1):
            if p[j - 1] != "*":
                break
            dp[0][j] = True
        
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] in {s[i - 1], "?"}:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                # 3rd case is p[j - 1] != s[i - 1], return False
                # but we already set it to false
        
        return dp[-1][-1]