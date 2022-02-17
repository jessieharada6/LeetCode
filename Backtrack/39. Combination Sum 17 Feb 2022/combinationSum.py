class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        
        def dfs(index, target, path):
            if target < 0:
                # return None
                # during recursion, it won't exit the current function
                # but to continue the current operation
                return 
            
            if target == 0:
                output.append(path)
                return
            
            # dfs() loops every element in the for loop starting from index to len of array
            for i in range(index, len(candidates)):
                # [1] + [2] produces a new array [1, 2]
                # start backtracking of the tree
                # i controls the range of index to len(candidates)
                dfs(i, target - candidates[i], path + [candidates[i]])
        
        dfs(0, target, [])
        return output


# to debug and test
# https://www.onlinegdb.com/online_python_debugger
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        
        def dfs(index, target, path):
            if target < 0:
                # return None
                return 
            
            if target == 0:
                output.append(path)
                return
            
            # dfs() loops every element in the for loop starting from index
            for i in range(index, len(candidates)):
                # [1] + [2] produces a new array [1, 2]
                # start backtracking of the tree
                dfs(i, target - candidates[i], path + [candidates[i]])
        
        dfs(0, target, [])
        return output

class_instance = Solution()
l = class_instance.combinationSum([2, 3, 6, 7], 7)
print(l)

if l == [[2,2,3],[7]]:
    print("Correct")
else:
    print("Incorrect")
    
