class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        if len(quantities) == n:
            return max(quantities)
        
        def getShops(m, quantities):
            shops = 0
            for q in quantities:
                shops += (q - 1) // m + 1
            return shops
        
        l, r = 0, max(quantities) + 1
        while l + 1 < r:
            m = (l + r) // 2
            if getShops(m, quantities) <= n:
                r = m
            else:
                l = m
        return r