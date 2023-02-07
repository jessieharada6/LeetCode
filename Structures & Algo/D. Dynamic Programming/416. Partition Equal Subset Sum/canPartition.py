# 2. 
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2: return False
        
        @cache
        def dfs(start, s) -> bool:
            if s * 2 > total:
                return False 

            if start == n:
                return s * 2 == total

            return dfs(start + 1, s + nums[start]) or dfs(start + 1, s)

        return dfs(0, 0)

# 3. 
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2: return False
        target = total / 2

        @cache
        def dfs(start, s) -> bool:
            if s > target:
                return False 

            if start == n:
                return s == target

            return dfs(start + 1, s + nums[start]) or dfs(start + 1, s)

        return dfs(0, 0)

# 4. 
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2: return False
        target = total // 2

        f = set()                       # set不能在iterate时加入元素 所以需要cur_f
        f.add(0)                        # dfs(0,0)

        for num in nums:
            cur_f = set()

            for s in f:
                cur_f.add(s)            # dfs(start + 1, s)
                cur_f.add(s + num)      # dfs(start + 1, s + nums[i])

            if target in cur_f:
                return True
            f = cur_f

        return False


