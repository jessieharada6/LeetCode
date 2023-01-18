class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def isPalindrome(s, i, j):
            while i < j:
                if s[i] != s[j]: return False
                i += 1
                j -= 1
            return True
            

        def dfs(path, i):
            if i == len(s):
                ans.append(path)
                return

            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    dfs(path + [s[i:j + 1]], j + 1)
        
        dfs([], 0)
        return ans

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]: return False
                l += 1
                r -= 1
            return True

        paths = []
        def dfs(path, i):
            # print(path, i)
            if i == len(s):
                paths.append(path[:])
                
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    path.append(s[i:j + 1])
                    dfs(path, j + 1)
                    path.pop()
                    
        
        dfs([], 0)
        return paths

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
                
            for j in range(i, len(s)): # 之前走过的substring不再走？始终i为起点 j向右看
                if isPalindrome(s, i, j): # 给定判断范围
                    dfs(path + [s[i : j + 1]], j + 1) # 横向往右推动，不需要vis？因为j+1（i）时会给定下一个起点 再由j向右推动
                    
        dfs([], 0)
        return ans
        # combination? 不是单纯的combination也有全排列但是不回头的全排列