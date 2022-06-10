class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        paths = []
        n = len(candidates)
        candidates.sort()
        
        def traverse(path, index, target):
            # print(path, target, index)
            if target < 0:
                return
            
            if target == 0:
                paths.append(path[:])
                return
            
            for i in range(index, n):   ### note
                # i > index to ensure different elements, not i == index
                # starting from i and i - 1, subtree is the same
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                # Each number in candidates may only be used once in the combination.
                traverse(path, i + 1, target - candidates[i])
                path.pop()
        
        traverse([], 0, target)
        return paths