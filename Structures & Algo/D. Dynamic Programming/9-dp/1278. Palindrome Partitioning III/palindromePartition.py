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