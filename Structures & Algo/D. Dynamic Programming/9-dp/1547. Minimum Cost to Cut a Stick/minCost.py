class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        @cache
        def dfs(l, r):
            if l + 1 >= r: return 0 # e.g. l = 1 r = 2 不能再切了
            res = inf
            for cut in cuts:
                if l < cut < r: # 关键 - l必须小于cut 否则切不了 r同理
                    res = min(res, dfs(l, cut) + dfs(cut, r) + r - l) # r - l 当前段 + 未来的切掉的左边和右边
            return 0 if res == inf else res # e.g. 当l==cut, res = inf
        
        return dfs(0, n)

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]

        @cache
        def dfs(l ,r):
            res = inf
            for i in range(l + 1, r):
                res = min(res, dfs(l, i) + dfs(i, r))
            res += cuts[r] - cuts[l]
            return 0 if res == inf else res

        
        return dfs(0, len(cuts) - 1)

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]

        @cache
        def dfs(l ,r):
            res = inf
            for i in range(l + 1, r):
                res = min(res, dfs(l, i) + dfs(i, r) + cuts[r] - cuts[l])
            return 0 if res == inf else res

        
        return dfs(0, len(cuts) - 1)