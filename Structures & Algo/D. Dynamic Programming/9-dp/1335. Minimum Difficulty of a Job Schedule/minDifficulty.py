class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n: return -1
        if d == n: return sum(jobDifficulty)

        def getDifficulty(l, r):
            return max(jobDifficulty[l : r + 1])
        
        @cache
        def dfs(left, d):
            if d == 1: return getDifficulty(left, n - 1)
            return min(getDifficulty(left, nextLeft - 1) + dfs(nextLeft, d - 1) for nextLeft in range(left + 1, n - d + 2))
        
        return dfs(0, d)
    
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n: return -1
        if d == n: return sum(jobDifficulty)

        def getDifficulty(l, r):
            return max(jobDifficulty[l : r + 1])
        
        @cache
        def dfs(left, d):
            if d == 1: return getDifficulty(left, n - 1)
            res = inf
            for nextLeft in range(left + 1, n - d + 2):
                res = min(res, getDifficulty(left, nextLeft - 1) + dfs(nextLeft, d - 1)) 
            return res
        
        return dfs(0, d)