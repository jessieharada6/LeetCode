class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        paths = []
        n = len(candidates)
        
        def traverse(path, index, target):
            # print(path, target, index)
            if target < 0:
                return
            
            if target == 0:
                paths.append(path[:])
                return
            
            # traverse left to right, index controls i's starting value, 
            # so i won't go from 0 everytime -- if (index, n):[[2,2,3],[7]]
            #                                 if just (n): [[2,2,3],[2,3,2],[3,2,2],[7]]
            for i in range(index, n):   ### note     
                path.append(candidates[i])
                # The same number may be chosen from candidates an unlimited number of times. 
                traverse(path, i, target - candidates[i])
                path.pop()
        
        traverse([], 0, target)
        return paths