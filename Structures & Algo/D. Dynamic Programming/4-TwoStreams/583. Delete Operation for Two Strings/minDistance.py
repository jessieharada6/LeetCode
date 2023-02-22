class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # @cache
        # def dfs(i, j) -> int:
        #     if i == 0 or j == 0: return i + j

        #     if word1[i - 1] == word2[j - 1]: return dfs(i - 1, j - 1)
        #     return 1 + min(dfs(i - 1, j),dfs(i, j - 1))

        # return dfs(m, n)

        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    f[i][j] = i + j
                elif word1[i - 1] == word2[j - 1]: 
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = 1 + min(f[i - 1][j], f[i][j - 1])
        return f[-1][-1]
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # @cache
        # def dfs(i, j) -> int:
        #     if i < 0 or j < 0: return i + j + 2

        #     if word1[i] == word2[j]: return dfs(i - 1, j - 1)
        #     return 1 + min(dfs(i - 1, j),dfs(i, j - 1))

        # return dfs(m - 1, n - 1)

        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1): f[i][0] = i
        for j in range(n + 1): f[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]: 
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = 1 + min(f[i - 1][j], f[i][j - 1])
        return f[-1][-1]