class Solution:
    def minDifficulty(self, jobDifficulty: List[int], D: int) -> int:
        n = len(jobDifficulty)
        if D > n: return -1
        if D == n: return sum(jobDifficulty)

        def getDifficulty(l, r):
            return max(jobDifficulty[l : r + 1])
        
        # @cache
        # def dfs(left, d):
        #     if d == 1: return getDifficulty(left, n - 1)
        #     res = inf
        #     maxDiff = 0
        #     for nextLeft in range(left + 1, n - d + 2):
        #         maxDiff = max(maxDiff, jobDifficulty[nextLeft - 1])
        #         res = min(res, maxDiff + dfs(nextLeft, d - 1))
        #     return res
        
        # return dfs(0, D)

        f = [[0] * (D + 1) for _ in range(n)]
        for left in range(n - 1, -1, -1):
            for d in range(1, min(D + 1, n - left + 1)):
                if d == 1: f[left][d] = getDifficulty(left, n - 1)
                else:
                    res = inf
                    maxDiff = 0
                    for nextLeft in range(left + 1, n - d + 2):
                        maxDiff = max(maxDiff, jobDifficulty[nextLeft - 1])
                        res = min(res, maxDiff + f[nextLeft][d - 1])
                    f[left][d] = res
        return f[0][D]


# -------------------------------
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