class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # @cache
        # def dfs(i, j) -> int:
        #     if i < 0 or j < 0: return 0

        #     if text1[i] == text2[j]:
        #         return dfs(i - 1, j - 1) + 1
        #     return max(dfs(i - 1, j), dfs(i, j - 1))
        
        # return dfs(m - 1, n - 1)

        f = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    f[i][j] = 1 + (f[i - 1][j - 1] if i-1>=0 and j-1>=0 else 0)
                else:
                    f[i][j] = max(f[i - 1][j] if i-1>=0 else 0, f[i][j - 1] if j-1>=0 else 0)
        return f[-1][-1]