class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m == n and s == t: return 1   # just nice match
        if m < n: return 0    # if s is shorter, not enough characters to match
                              # distinct: 每一次都会向前移动i
        # @cache
        # def dfs(i, j) -> int:
        #     if j >= 0 and i < 0: return 0   # s has reached its end, without matching the entire t
        #     if j < 0: return 1              # t has reached its end
        #     if s[i] == t[j]: return dfs(i - 1, j - 1) + dfs(i - 1, j) # 2 options, remove both chars or see if t[j] == s[i - 1]

        #     return dfs(i - 1, j)

        # return dfs(m - 1, n - 1)

        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1): f[i][0] = 1 # j < 0: when "" for both s and t (won't occur based on constraints), there is 1 match
        for j in range(1, n + 1): f[0][j] = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    f[i][j] = f[i - 1][j - 1] + f[i - 1][j]
                else:
                    f[i][j] = f[i - 1][j]
        return f[-1][-1]