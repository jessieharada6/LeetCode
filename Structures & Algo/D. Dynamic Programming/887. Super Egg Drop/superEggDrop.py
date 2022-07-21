class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        memo = dict()
        @lru_cache(None)
        def dp(k, n):
            if n == 0 or n == 1: return n
            if k == 1: return n
            
            if (k, n) in memo:
                return memo[(k, n)]
            
            res = float("INF")
            lo, hi = 1, n
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                broken = dp(k - 1, mid - 1)
                not_broken = dp(k, n - mid)
                
                if broken > not_broken:
                    hi = mid - 1
                    res = min(res, broken + 1)
                else:
                    lo = mid + 1
                    res = min(res, not_broken + 1)
                    
            # for i in range(1, n + 1):
            #     res = min(res, max(dp(k - 1, i - 1), dp(k, n - i)) + 1)
            
            memo[(k, n)] = res
            return res
        
        return dp(k, n)
                    

#TLE
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        memo = dict()
        def dp(k, n):
            res = math.inf
            if n == 0 or n == 1: return n
            if k == 1: return n
            
            if (k, n) in memo:
                return memo[(k, n)]
            
            for i in range(1, n + 1):
                res = min(res, max(dp(k - 1, i - 1), dp(k, n - i)) + 1)
            
            memo[(k, n)] = res
            return res
        
        return dp(k, n)