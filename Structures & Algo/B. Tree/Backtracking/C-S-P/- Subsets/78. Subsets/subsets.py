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