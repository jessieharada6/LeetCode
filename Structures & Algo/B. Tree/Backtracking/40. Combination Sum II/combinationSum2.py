class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        paths = []
        n = len(candidates)
        candidates.sort()           ### note
        
        def traverse(path, index, target):
            # print(path, target, index)
            if target < 0:
                return
            
            if target == 0:
                paths.append(path[:])
                return
            
            for i in range(index, n):   ### note                            ### traverse left to right
                # i > index to ensure different elements, not i == index
                # starting from i and i - 1, subtree is the same
                if i > index and candidates[i] == candidates[i - 1]:        # cut repeating tree layer (traversed before)
                    # print(i, index)
                    continue
                path.append(candidates[i])
                # print(path, i, index)
                # Each number in candidates may only be used once in the combination.
                traverse(path, i + 1, target - candidates[i])               # ### traverse top down
                path.pop()
        
        traverse([], 0, target)
        return paths