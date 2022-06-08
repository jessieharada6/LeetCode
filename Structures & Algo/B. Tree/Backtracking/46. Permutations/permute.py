class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        paths = []
        # path = []
        n = len(nums)
        
        def traverse(nums, path):
            if len(path) == n:
                paths.append(path[:])
                return
            
            for i in nums:
                if i in path:
                    continue
                path.append(i)
                traverse(nums, path)
                path.pop()
            
        
        traverse(nums, [])
        
        return paths


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        paths = []
        n = len(nums)
        
        def traverse(nums, path):
            if len(path) == n:
                paths.append(path[:])
                return
            
            for i in nums:
                if i in path:
                    continue
                path.append(i)
                traverse(nums, path)
                path.pop()
            
        
        for i in nums:
            traverse(nums, [i])
        
        return paths