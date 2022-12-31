class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def dfs(i, path):
            if i > n + 1: return
            if i == n + 1 and len(path) == k:
                ans.append(path)
                return
            
            dfs(i + 1, path)
            dfs(i + 1, path + [i])
        
        dfs(1, [])
        return ans


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        
        def traverse(start, path):
            if len(path) == k:
                combinations.append(path[:])
            
            for i in range(start, n + 1):
                path.append(i)
                traverse(i + 1, path)
                path.pop()
        
        traverse(1, [])
        return combinations