class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        # @cache
        # def dfs(i):
        #     if i == n: return 0
        #     res, w, h = inf, 0, 0
        #     for j in range(i + 1, n + 1):
        #         w += books[j - 1][0]
        #         if w > shelfWidth: continue
        #         h = max(h, books[j - 1][1]) # max height for this layer
        #         res = min(res, h + dfs(j))  # min height sum for books
        #     return res
        # return dfs(0)

        f = [inf] * (n + 1)
        for i in range(n, -1, -1):
            if i == n: 
                f[i] = 0
                continue
            res, w, h = inf, 0, 0
            for j in range(i + 1, n + 1):
                w += books[j - 1][0]
                if w > shelfWidth: continue
                h = max(h, books[j - 1][1])
                res = min(res, h + f[j])
            f[i] = res
        return f[0]
    
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)

        # @cache
        # def dfs(left):
        #     if left == n: return 0
        #     res = inf
        #     h = 0
        #     w = 0
        #     for nxt in range(left + 1, n + 1):
        #         w += books[nxt - 1][0]
        #         if w > shelfWidth: continue
        #         h = max(h, books[nxt - 1][1])
        #         res = min(res, h + dfs(nxt))
        #     return res
        # return dfs(0)

        f = [inf] * n + [0]
        for left in range(n - 1, -1, -1):
            # if left == n: f[left] = 0
            res = inf
            h = 0
            w = 0
            for nxt in range(left + 1, n + 1):
                w += books[nxt - 1][0]
                if w > shelfWidth: continue
                h = max(h, books[nxt - 1][1])
                res = min(res, h + f[nxt])
            f[left] = res
        # print(f)
        return f[0]
        
        
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