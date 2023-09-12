class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        s = word1 + word2
        ans = 0
        @cache
        def dfs(i, j):
            nonlocal ans
            if i > j: return 0
            if i == j: return 1

            if s[i] == s[j]:
                res = dfs(i + 1, j - 1) + 2
                if i < m <= j: #both words需要非空 在i还在word1时记录
                    ans = max(ans, res)
                return res
            return max(dfs(i + 1, j), dfs(i, j - 1))
        dfs(0, len(s) - 1)
        return ans