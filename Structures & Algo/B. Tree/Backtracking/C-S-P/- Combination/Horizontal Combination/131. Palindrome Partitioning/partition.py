class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]: return False 
                l += 1
                r -= 1
            return True
        
        ans = []
        # vis = [False] * len(s)
        def dfs(path, i):
            if "".join(path) == s:
                ans.append(path)
                return
                
            for j in range(i, len(s)): # 之前走过的substring不再走
                if isPalindrome(s, i, j): # 给定判断范围
                    dfs(path + [s[i : j + 1]], j + 1) # 横向往右推动，不需要vis
                    
        dfs([], 0)
        return ans