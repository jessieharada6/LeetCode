class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        @cache
        def dfs(s):
            if not s: return True
            res = False
            for i in range(1, n + 1):
                if s[:i] in wordDict: # s[开始:i)是否在worddict中
                    res = dfs(s[i:]) or res #if in 就从s[i:)继续查看
            return res

        return dfs(s)