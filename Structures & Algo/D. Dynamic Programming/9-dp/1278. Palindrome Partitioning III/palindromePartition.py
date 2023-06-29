class Solution:
    def palindromePartition(self, s: str, K: int) -> int:
        n = len(s)
        # @cache
        # def cost(l, r):
        #     # change = 0
        #     # while l < r:
        #     #     change += s[l] != s[r]:
        #     #     l += 1
        #     #     r -= 1
        #     # return change
        #     if l >= r: return 0
        #     if s[l] == s[r]:
        #         return cost(l + 1, r - 1)
        #     else:
        #         return cost(l + 1, r - 1) + 1
        
        cost = [[0] * n for _ in range(n)]
        for l in range(n - 1, -1, -1):
            for r in range(l + 1, n):
                if s[l] == s[r]:
                    cost[l][r] = cost[l + 1][r - 1]
                else:
                    cost[l][r] = cost[l + 1][r - 1] + 1

        # @cache
        # def dfs(left, k):
        #     if k == 1: return cost(left, n - 1)
        #     return min(cost(left, nextLeft - 1) + dfs(nextLeft, k - 1) for nextLeft in range(left + 1, n - k + 2))
        
        # return dfs(0, K)

        f = [[0] * (K + 1) for _ in range(n)]
        for left in range(n - 1, -1, -1):
            for k in range(1, min(n - left + 1, K + 1)):
                if k == 1: f[left][k] = cost[left][n - 1]
                else: f[left][k] = min(cost[left][nextLeft - 1] + f[nextLeft][k - 1] for nextLeft in range(left + 1, n - k + 2))
        return f[0][K]


# ---------------------------------------------------------------
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)

        # 是否构成回文串，如果不，加字母个数
        @cache
        def cost(l, r):
            res = 0
            while l < r:
                res += s[l] != s[r] 
                l += 1
                r -= 1
            return res

        # left 当前切割点
        # k 剩下的需要切割的串
        @cache
        def dfs(left, k):
            if k == 1: return cost(left, n - 1)

            # nextLeft 下一个切割点
            return min(cost(left, nextLeft - 1) + dfs(nextLeft, k - 1) for nextLeft in range(left + 1, n - k + 2))
        
        return dfs(0, k)

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)

        # 是否构成回文串，如果不，加字母个数
        @cache
        def cost(l, r):
            if l >= r: return 0
            if s[l] == s[r]: return cost(l + 1, r - 1)
            else: return cost(l + 1, r - 1) + 1

        # # left 当前切割点
        # # k 剩下的需要切割的串
        @cache
        def dfs(left, k):
            if k == 1: return cost(left, n - 1)

            # nextLeft 下一个切割点
            return min(cost(left, nextLeft - 1) + dfs(nextLeft, k - 1) for nextLeft in range(left + 1, n - k + 2))
        
        return dfs(0, k)