class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        @cache
        def dfs(i):
            if i < 0: return 0

            res = inf
            res = 1 + dfs(i - 1)
            for j in range(i + 1):
                if s[j:i + 1] in dictionary:
                    res = min(res, dfs(j - 1))
            
            return res
        
        return dfs(len(s) - 1)