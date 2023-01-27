class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def dfs(target, path, start_index):
            if target < 0: return

            if target == 0:
                ans.append(path)
                return
            
            for j in range(start_index, len(candidates)):
                # 1.
                # start_index 是本次递归的起点 j > start_index表示的是之前的path已经填好 需要考虑的是从start_index为起点需要填入什么
                # 2.
                # candidates[j - 1]在(len(path))层填入 如果在上一次的一系列递归中已经找到了组合 ([1,2,5])
                # 那么当candidates[j - 1] == candidates[j]如果也让candidates[j]填入(len(path))层时 就会有重复的组合 ([1,2,5])
                # 这个condition避免当candidates[j - 1] == candidates[j]时，candidates[j]填入与candidates[j-1]相同的层数
                # 3.
                # 注意，如果candidates[j - 1]在len(path) - 1层填入，candidates[j]在len(path)层填入 是完全可以的 ([1,1,6])
                if j > start_index and candidates[j - 1] == candidates[j]:
                    continue
                dfs(target - candidates[j], path + [candidates[j]], j + 1)
        
        dfs(target, [], 0)
        return ans

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()
        
        def traverse(start, path, target):
            if target < 0:
                return
            
            if target == 0:
                combinations.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i - 1] == candidates[i]:
                    continue
                path.append(candidates[i])
                traverse(i + 1, path, target - candidates[i])
                path.pop()
        
        traverse(0, [], target)
        return combinations
        

        
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