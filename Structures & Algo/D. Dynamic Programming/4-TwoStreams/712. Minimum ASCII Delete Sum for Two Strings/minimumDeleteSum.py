class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        # @cache
        # def dfs(i, j) -> int:
        #     if i == 0 and j == 0: return 0
        #     if i == 0: return ord(s2[j - 1]) + dfs(i, j - 1) #return sum(ord(s2[left]) for left in range(j)) 
        #     if j == 0: return ord(s1[i - 1]) + dfs(i - 1, j) #return sum(ord(s1[left]) for left in range(i))

        #     if s1[i - 1] == s2[j - 1]: return dfs(i - 1, j - 1)
           
        #     return min(ord(s1[i - 1]) + dfs(i - 1, j), ord(s2[j - 1]) + dfs(i, j - 1))

        # return dfs(m, n)

        f = [[0] * (n + 1) for _ in range(m + 1)]
        # for i in range(1, m + 1): f[i][0] = ord(s1[i - 1]) + f[i - 1][0]  
        # for j in range(1, n + 1): f[0][j] = ord(s2[j - 1]) + f[0][j - 1]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0: continue
                if j == 0:
                    f[i][0] = ord(s1[i - 1]) + f[i - 1][0]  
                elif i == 0:
                    f[0][j] = ord(s2[j - 1]) + f[0][j - 1]
                elif s1[i - 1] == s2[j - 1]: 
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = min(ord(s1[i - 1]) + f[i - 1][j], ord(s2[j - 1]) + f[i][j - 1])
        return f[-1][-1]

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        # @cache
        # def dfs(i, j) -> int:
        #     if i < 0: return sum(ord(s2[left]) for left in range(j + 1)) O(n^2) -> 当i<0，j可以是3，2，1 每一次都是o(n)
        #     if j < 0: return sum(ord(s1[left]) for left in range(i + 1))

        #     if s1[i] == s2[j]: return dfs(i - 1, j - 1)
           
        #     return min(ord(s1[i]) + dfs(i - 1, j), ord(s2[j]) + dfs(i, j - 1))

        # return dfs(m - 1, n - 1)

        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1): f[i][0] = sum(ord(s1[left]) for left in range(i)) # o(n^2)
        for j in range(1, n + 1): f[0][j] += sum(ord(s2[left]) for left in range(j))
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]: 
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = min(ord(s1[i - 1]) + f[i - 1][j], ord(s2[j - 1]) + f[i][j - 1])
        
        return f[-1][-1]