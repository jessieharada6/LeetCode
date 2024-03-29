class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(start_index, path, target):
            if target < 0: return
            if target == 0:
                ans.append(path)
            
            for j in range(start_index, len(candidates)):
                dfs(j, path + [candidates[j]], target - candidates[j]) # 这个放stat_index会一直重复用candidates[0]不能往右移动
        
        dfs(0, [], target)
        return ans
        
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(path, i):
            if sum(path) > target: return

            if sum(path) == target:
                ans.append(path)
                return

            for j in range(i, len(candidates)):
                dfs(path + [candidates[j]], j)
            
        dfs([], 0)
        return ans


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        
        def traverse(start, path, target):
            if target < 0:
                return
            
            if target == 0:
                combinations.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                traverse(i, path, target - candidates[i])
                path.pop()
        
        traverse(0, [], target)
        return combinations

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        paths = []
        
        def traverse(start, path):
            if sum(path) == target:
                paths.append(path[:])
                return
            
            if sum(path) > target:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                traverse(i, path)
                path.pop()
        
        traverse(0, [])
        return paths

### 1. 枚举当前选哪个
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        paths = []
        n = len(candidates)
        def dfs(start, path):
            if sum(path) > target:
                return
            if sum(path) == target:
                paths.append(path)
                return

            for i in range(start, n):
                dfs(i, path + [candidates[i]])
            
        dfs(0, [])
        return paths

# 2. 选与不选
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        paths = []
        n = len(candidates)
        def dfs(start, path):
            if start == n:
                return
            if sum(path) > target:
                return
            if sum(path) == target:
                paths.append(path)
                return

            dfs(start, path + [candidates[start]]) # 选 start留在当前
            dfs(start + 1, path) # 不选 start去下一个
            
        dfs(0, [])
        return paths