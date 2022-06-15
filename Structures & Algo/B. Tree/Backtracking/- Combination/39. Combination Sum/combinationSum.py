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
        combinations = []
        
        def traverse(start, path, target):
            if target < sum(path):
                return
            
            if target == sum(path):
                combinations.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                traverse(i, path, target)
                path.pop()
        
        traverse(0, [], target)
        return combinations
        