## def dfs(start, s) -> bool: # 能否让已选的数的和(s)与待选的数(下标>start)的和为target
# 1. s starts from 0
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2: return False
        target = total // 2

        @cache
        def dfs(start, s) -> bool: 
            if s > target: return False
            if start == n: return s == target

            return dfs(start + 1, s + nums[start]) or dfs(start + 1, s)

        
        return dfs(0, 0)

## def dfs(start, left) -> bool：(已选数已选并已经减去)能否在剩余待选的数字中选出和为left的数
# 2. s is from target downwards
class Solution:
    def canPartition(self, nums: List[int]) -> bool: 
        n = len(nums)
        total = sum(nums)
        if total % 2: return False
        target = total // 2

        @cache
        def dfs(start, left) -> bool: 
            if left < 0: return False
            if start == n: 
                return left == 0

            return dfs(start + 1, left - nums[start]) or dfs(start + 1, left)

        
        return dfs(0, target)

# 3. use array as cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2: return False
        target = total // 2

        # cache[start][left] 
        # start: [0, n-1]     到达n-1结束 n时已做出判断（if start == n）
        # left: [0, target] 从target开始向下走
        cache = [[-1] * (target + 1) for _ in range(n)]
        def dfs(start, left) -> bool: 
            if start == n: return left == 0
            if left < 0: return False

            if cache[start][left] != -1: return cache[start][left]

            res = dfs(start + 1, left - nums[start]) or dfs(start + 1, left)
            cache[start][left] = res
            return res

        return dfs(0, target)

# 4. imitate dp
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2: return False
        target = total // 2

        # cache[start][left] 
        # start: [0, n]     从n开始往下走
        # left: [0, target] 从target开始向下走
        cache = [[-1] * (target + 1) for _ in range(n + 1)]
        def dfs(start, left) -> bool: 
            if start == 0: return left == 0
            if left < 0: return False

            if cache[start][left] != -1: return cache[start][left]

            res = dfs(start - 1, left - nums[start - 1]) or dfs(start - 1, left)
            cache[start][left] = res
            return res

        return dfs(n, target)

# 5. 
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2: return False
        target = total // 2

        f = [[False] * (target + 1) for _ in range(n + 1)]
        for start in range(n + 1): f[start][0] = True # 当还未开始进入数组循环 且 剩余是0
        for start in range(1, n + 1):
            for left in range(1, target + 1):
                if left - nums[start - 1] >= 0:
                    f[start][left] = f[start - 1][left - nums[start - 1]] or f[start - 1][left] 
                else:
                    f[start][left] = f[start - 1][left] # 如果<0 就不选这个数
        return f[n][target]


##########################################################################################
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

            if start == n: #数字已经选完
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


