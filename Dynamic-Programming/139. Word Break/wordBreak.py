class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for _ in range(n + 1)]
        dp[0] = True
        
        max_len = 0
        for word in wordDict:
            max_len = max(max_len, len(word))

        for i in range(1, n + 1):
            for j in range(0, i):
                if i - j > max_len:
                    continue
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        
        return dp[-1]