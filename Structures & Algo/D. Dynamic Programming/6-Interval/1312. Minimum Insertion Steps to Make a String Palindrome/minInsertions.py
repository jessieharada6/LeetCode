class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        # @cache
        # def dfs(l, r) -> int:
        #     if l >= r: return 0 # l > r 已检查完 l == r 相遇

        #     if s[l] == s[r]:
        #         return dfs(l + 1, r - 1)
        #     return 1 + min(dfs(l + 1, r), dfs(l, r - 1))
        # return dfs(0, n - 1)

        # ^              r - 1  r  >
        # l                x    o
        # l + 1            x    x
        f = [[0] * n for _ in range(n)]
        for l in range(n - 1, -1, -1):
            f[l][l] = 0
            # l > r: f 起始值覆盖 l == r: 上一排覆盖 l < r: 剩下的情况即r > l，r覆盖[l+1, n)的范围
            for r in range(l + 1, n):
                if s[l] == s[r]:
                    f[l][r] = f[l + 1][r - 1]
                else:
                    f[l][r] = 1 + min(f[l + 1][r], f[l][r -1])
        return f[0][n - 1]
