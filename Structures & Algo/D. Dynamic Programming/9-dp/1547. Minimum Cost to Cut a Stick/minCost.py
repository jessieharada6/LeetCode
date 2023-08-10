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