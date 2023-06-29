class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)

        # @cache
        # def dfs(left):
        #     if left < 0: return 0
        #     res = inf
        #     h = 0
        #     w = 0
        #     for cur in range(left, -1, -1):
        #         w += books[cur][0]
        #         if w > shelfWidth: continue
        #         h = max(h, books[cur][1])
        #         res = min(res, h + dfs(cur - 1))
        #     return res
        # return dfs(n - 1)

        f = [0] + [inf] * n  #只修改与f有关的下标 向上加1
        for left in range(n): # 循环f
            h = 0
            w = 0
            res = inf
            for cur in range(left, -1, -1):
                w += books[cur][0]
                if w > shelfWidth: continue
                h = max(h, books[cur][1])
                res = min(res, h + f[cur])
            f[left + 1] = res #赋值f
        return f[n]