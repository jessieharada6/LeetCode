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
        used = [0 for _ in range(n)]
        
        def traverse(path):
            if len(path) == n:
                paths.append(path[:])
                return                  # base case, track up to the tree
            
            for i in range(n):
                if used[i]: continue
                used[i] = True
                path.append(nums[i])
                # print("before", i, path) # i is the index of the last num in the permutation
                traverse(path)
                # print("after", i, path)
                path.pop()
                used[i] = False
        
        traverse([])
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