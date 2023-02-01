# 1. 回溯
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        paths = []

        def dfs(start, path):
            # print(start ,path)
            if sum(path) > n:
                return
            
            if sum(path) == n:
                if len(path) == k:
                    paths.append(path)
                return
            
            for i in range(start, 10):
                dfs(i + 1, path + [i])
        
        dfs(1, [])
        return paths

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def dfs(start_index, path, n):
            if len(path) > k: return
            if len(path) == k:
                if n == 0:
                    ans.append(path)
            
            for j in range(start_index, 10):
                dfs(j + 1, path + [j], n - j)
        
        dfs(1, [], n)
        return ans

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combinations = []
        
        def traverse(start, path, n):
            if n < 0:
                return
            
            if n == 0 and len(path) == k:
                combinations.append(path[:])
                return
            
            for i in range(start, 10):
                path.append(i)
                traverse(i + 1, path, n - i)
                path.pop()
        
        traverse(1, [], n)
        return combinations

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        paths = []
        
        def traverse(start, path):
            if sum(path) == n and len(path) == k:
                paths.append(path[:])
                return
            
            if sum(path) > n:
                return
            
            for i in range(start, 10):
                path.append(i)
                traverse(i + 1, path)
                path.pop()
            
        traverse(1, [])
        return paths


# 2. 选与不选
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        paths = []

        def dfs(start, path):
            # print(start ,path)
            if start > 10:
                return
            
            if sum(path) > n:
                return
            
            if sum(path) == n:
                if len(path) == k:
                    paths.append(path)
                return
            
            dfs(start + 1, path + [start])
            dfs(start + 1, path)
        
        dfs(1, [])
        return paths