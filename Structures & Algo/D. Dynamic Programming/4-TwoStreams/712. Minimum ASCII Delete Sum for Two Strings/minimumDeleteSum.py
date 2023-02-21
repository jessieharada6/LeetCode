class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        # @cache
        # def dfs(i, j) -> int:
        #     if i < 0: return sum(ord(s2[left]) for left in range(j + 1))
        #     if j < 0: return sum(ord(s1[left]) for left in range(i + 1))

        #     if s1[i] == s2[j]: return dfs(i - 1, j - 1)
           
        #     return min(ord(s1[i]) + dfs(i - 1, j), ord(s2[j]) + dfs(i, j - 1))

        # return dfs(m - 1, n - 1)

        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1): f[i][0] = sum(ord(s1[left]) for left in range(i))
        for j in range(1, n + 1): f[0][j] += sum(ord(s2[left]) for left in range(j))
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]: 
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = min(ord(s1[i - 1]) + f[i - 1][j], ord(s2[j - 1]) + f[i][j - 1])
        
        return f[-1][-1]