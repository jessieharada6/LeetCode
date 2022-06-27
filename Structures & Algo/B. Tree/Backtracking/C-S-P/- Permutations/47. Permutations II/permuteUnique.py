class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False for _ in range(n)]
        nums.sort()
        
        paths = []
        
        def traverse(path):
            if len(path) == n:
                paths.append(path[:])
                return
            
            for i in range(n):
                if used[i]: continue
                ### note: efficiency using not used[i - 1] (better) vs used[i - 1]
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]: continue
                used[i] = True
                path.append(nums[i])
                traverse(path)
                path.pop()
                used[i] = False
        
        traverse([])
        return paths


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        paths = []
        used = [False for _ in range(n)]
        
        def traverse(path):
            if len(path) == n:
                paths.append(path[:])
                return
            
            prevNum = -66
            
            for i in range(n):
                if used[i]: continue
                if prevNum == nums[i]: continue
                
                used[i] = True
                path.append(nums[i])
                prevNum = nums[i]
                traverse(path)
                path.pop()
                used[i] = False
        
        traverse([])
        return paths