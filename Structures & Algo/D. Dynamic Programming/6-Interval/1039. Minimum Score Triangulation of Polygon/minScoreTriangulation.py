class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        # 原问题：以 values 表示的多边形的分数
        # 最后一次剖分出的三角形的一条边一定是 0~n-1: min(values[0] * values[n - 1] * values[i], dfs(l, i), dfs(i, r))
        # 子问题 剖分出的三角形的一条边一定是 i~j
        n = len(values)
        # @cache
        # def dfs(l, r) -> int:
        #     if r - l < 2: return 0
        #     res = inf
        #     for i in range(l + 1, r): # skip l and r 因为他们是会被用到的点
        #         cur = values[i] * values[l] * values[r] + dfs(l, i) + dfs(i, r)
        #         res = min(cur, res)
        #     return res
        
        # return dfs(0, n - 1)


        f = [[0] * n for _ in range(n)]
        for l in range(n - 1, -1, -1):
            for r in range(l + 2, n):
                res = inf
                # if r < l + 2: continue
                for i in range(l + 1, r):
                    cur = values[i] * values[l] * values[r] + f[l][i] + f[i][r]
                    res = min(res, cur)
                f[l][r] = res
        return f[0][n - 1]