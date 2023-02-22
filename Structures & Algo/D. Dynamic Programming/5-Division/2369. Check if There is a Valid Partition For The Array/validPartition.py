class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        def check_pair(i):
            return i - 1 >= 0 and nums[i] == nums[i - 1]
        def check_triplet(i):
            return i - 2 >= 0 and nums[i] == nums[i - 1] == nums[i - 2] \
            or (nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2)

        # @cache
        # def dfs(i) -> bool:
        #     if i < 0: return True
            
        #     res = False
        #     if check_pair(i): 
        #         res = dfs(i - 2) or res
        #     if check_triplet(i): 
        #         res = dfs(i - 3) or res
        #     return res

        # return dfs(n - 1)
        
        # @cache
        # def dfs(i) -> bool:
        #     if i == 0: return True
            
        #     res = False
        #     if check_pair(i - 1): 
        #         res = dfs(i - 2) or res
        #     if check_triplet(i - 1): 
        #         res = dfs(i - 3) or res
        #     return res

        # return dfs(n)

        f = [False] * (n + 1)
        f[0], f[1] = True, False # index: -1, 0
        f[2] = nums[0] == nums[1] # index: 1 - 2 <= n <= 10^5
        
        res = False
        for i in range(3, n + 1):
            res = False
            if check_pair(i - 1): 
                res = f[i - 2] or res
            if check_triplet(i - 1): 
                res = f[i - 3] or res
            f[i] = res

        return f[-1]

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        @cache
        def dfs(i, j) -> bool:
            if i < 0 and j < 0: return True
            if i < 0 and j > 0: return False
            if i > 0 and j < 0: return False
           
            if j - i + 1 == 2:
                if nums[i] != nums[j]: 
                    return False
                else: 
                    return dfs(i - 2, j - 2) or dfs(i - 3, j - 2) 

            if j - i + 1 == 3:
                if (nums[i] != nums[i + 1] or nums[i + 1]!= nums[i + 2]) \
                and (nums[i] + 1 != nums[i + 1] or nums[i + 1] + 1  != nums[i + 2]):
                    return False
                else:
                    return dfs(i - 3, j - 3) or dfs(i - 2, j - 3)
        
        return dfs(n - 2, n - 1) or dfs(n - 3, n - 1)
        
