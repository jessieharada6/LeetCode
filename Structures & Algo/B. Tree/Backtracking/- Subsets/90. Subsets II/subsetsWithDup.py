class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sets = []
        nums.sort()
        
        def traverse(start, path):
            sets.append(path[:])
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                traverse(i + 1, path)
                path.pop()
        
        traverse(0, [])
        return sets