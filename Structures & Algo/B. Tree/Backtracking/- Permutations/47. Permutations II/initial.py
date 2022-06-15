class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        paths = []
        
        def traverse(path, nums):
            if not nums and path not in paths:
                paths.append(path[:])
                return
            
            for i in range(len(nums)):
                traverse(path + [nums[i]], nums[:i] + nums[i + 1:])
        
        traverse([], nums)
        return paths


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        paths = []
        n = len(nums)
        used = [False for _ in range(n)]
        
        
        def traverse(path, used, nums):
            if len(path) == n and path not in paths:
                paths.append(path[:])
                return
            
            for i in range(n):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                traverse(path, used, nums)
                used[i] = False
                path.pop()
        
        traverse([], used, nums)
        return paths