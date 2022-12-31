class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(path, i):
            if i == len(nums):
                ans.append(path)
                return None # stop at this point, go back

            # order can change
            dfs(path, i + 1)
            dfs(path + [nums[i]], i + 1)
            
        
        dfs([], 0)
        return ans

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        def dfs(i):
            if i == len(nums):
                ans.append(path[:])
                return None 

            dfs(i + 1)

            path.append(nums[i])
            dfs(i + 1)
            path.pop()
            
        
        dfs(0)
        return ans
            

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = []
        
        def traverse(path, start):
            sets.append(path[:])                
            
            for i in range(start, len(nums)):   # terminal condition/base case: when index == len(nums)
                path.append(nums[i])
                # print(start, i, path, nums[i])
                traverse(path, i + 1)
                path.pop()
        
        traverse([], 0)
        return sets