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

# https://leetcode.cn/problems/permutations/solution/hui-su-suan-fa-by-powcai-2/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        paths = []
        
        def traverse(path, nums):
            if not nums:
                paths.append(path[:])
                return
            
            for i in range(len(nums)):
                # print("before", nums[i], nums)
                traverse(path + [nums[i]], nums[:i] + nums[i + 1:])
                # print("after", nums[i], nums)
        
        traverse([], nums)
        return paths