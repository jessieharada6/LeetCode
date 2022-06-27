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
        