class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        """
        1. 梳理清楚子问题是什么

        一开始的范围是 [1,n - 1]
        回文子序列一定在 [1,n]

        第一步：看left和right所在的位置是否相同

        范围会变小
        举例+分类讨论：  bbbab
        两种情况（要猜测的数字） 
            相同：dfs(i + 1, j - 1) + 2
            不相同: max(dfs(i + 1, j) , dfs(i, j - 1) )


        2. 整理：要解决的问题是在 [l,r] 内找回文子序列，
        目标：在顺序并且可以跳跃的情况下(子序列特性),最长的回文
        base case: l == r 返回1, l > r,l < 0, r < 0, l == n, r == n 返回0

        q1143
        """
        # @cache
        # def dfs(left, right):
        #     if left < 0 or right < 0 or left == n or right == n or left > right:
        #         return 0
        #     if left == right:
        #         return 1

        #     if s[left] == s[right]:
        #         return dfs(left + 1, right - 1) + 2
        #     return max(dfs(left + 1, right), dfs(left, right - 1))
        # return dfs(0, n - 1)

        f = [[0] * (n) for _ in range(n)]
        for i in range(n):
            f[i][i] = 1
        
        # left <---- base case (l == r) ----> right 
        # 从base case向两边算,left要倒着开始
        for left in range(n - 1, -1, -1): 
            # left + 1 开始 因为left == right返回1,left < right返回0
            for right in range(left + 1, n):
                # if left == right: f[left][right] = 1 # base case需要在开始前设置好 如果是"a" 不会进入循环
                if s[left] == s[right]:
                    f[left][right] = f[left + 1][right - 1] + 2
                else:
                    f[left][right] = max(f[left + 1][right], f[left][right - 1]) 
        return f[0][n - 1]

        # @cache
        # def dfs(left, right):
        #     if left > right:
        #         return 0
        #     if left == right:
        #         return 1

        #     if s[left] == s[right]:
        #         return dfs(left + 1, right - 1) + 2
        #     return max(dfs(left + 1, right), dfs(left, right - 1))
        # return dfs(0, n - 1)

        # f = [[0] * (n) for _ in range(n)]
        
        # for left in range(n - 1, -1, -1): 
        #     for right in range(left, n):
        #         if left == right:
        #             f[left][left] = 1; continue
        #         if s[left] == s[right]:
        #             f[left][right] = f[left + 1][right - 1] + 2
        #         else:
        #             f[left][right] = max(f[left + 1][right], f[left][right - 1]) 
        # return f[0][n - 1]


        f = [[0] * (n) for _ in range(n)]

        for left in range(n - 1, -1, -1): 
            f[left][left] = 1
            for right in range(left + 1, n):
                if s[left] == s[right]:
                    f[left][right] = f[left + 1][right - 1] + 2
                else:
                    f[left][right] = max(f[left + 1][right], f[left][right - 1]) 
        return f[0][n - 1]

        