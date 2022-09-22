class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        d = abs(endPos - startPos)
        if d > k or d % 2 != k % 2:
            return 0
        
        MOD = 10 ** 9 + 7
        
        @cache
        def dp(x, left):
            if abs(x - endPos) > left:
                return 0
            if left == 0:
                return 1
            
            return (dp(x - 1, left - 1) + dp(x + 1, left - 1)) % MOD
        
        return dp(startPos, k)


class Solution:
    def numberOfWays(self, startPos, endPos, k) -> int:
        d = abs(endPos - startPos)
        if d > k or d % 2 != k % 2:
            return 0
        
        MOD = 10 ** 9 + 7
        return comb(k, (d + k) // 2) % MOD