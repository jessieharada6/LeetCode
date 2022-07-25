class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        m = len(ring)
        n = len(key)
        
        ringDict = defaultdict(list)
        for i, r in enumerate(ring):
            ringDict[r].append(i)
        
        memo = [[-1] * n for _ in range(m)]
        
        def dp(i, j):
            if j == n: return 0
            
            res = math.inf
            
            if memo[i][j] != -1: return memo[i][j]
            
            for k in ringDict[key[j]]:
                delta = abs(k - i)
                delta = min(delta, m - delta)
                sub = dp(k, j + 1)       
                res = min(res, 1 + delta + sub)
            
            memo[i][j] = res
            return res
        

        return dp(0, 0)