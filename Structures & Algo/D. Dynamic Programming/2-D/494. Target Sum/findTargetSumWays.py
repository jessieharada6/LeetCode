## def dfs(start, left) -> int:
## 待选的数字之和会否等于t
# 1. 
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n, total = len(nums), sum(nums)
        if (target + total) % 2: return 0
        t = (target + total) // 2
        
        @cache
        def dfs(start, left) -> int:
            if start == 0 and left == 0: return 1
            if left < 0 or start == 0: return 0

            return dfs(start - 1, left - nums[start - 1]) + dfs(start - 1, left)

        return dfs(n, t)

# 2.
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n, total = len(nums), sum(nums)
        if (target + total) % 2: return 0
        t = (target + total) // 2
        if t < 0: return 0

        f = [[0] * (t + 1) for _ in range(n + 1)]
        f[0][0] = 1                      # if start == 0 and left == 0: return 1
        
        for start in range(1, n + 1):
            for left in range(0, t + 1): # 从0开始：left == 0 and start != 0
                if left - nums[start - 1] >= 0:
                    f[start][left] = f[start - 1][left - nums[start - 1]] + f[start - 1][left]
                else:
                    f[start][left] = f[start - 1][left]

        return f[n][t]

# 3.
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n, total = len(nums), sum(nums)
        if (target + total) % 2: return 0
        t = (target + total) // 2
        if t < 0: return 0

        f = [[0] * (t + 1) for _ in range(2)]
        f[0][0] = 1                      
        
        for start in range(1, n + 1):
            for left in range(0, t + 1): 
                if left - nums[start - 1] >= 0:
                    f[start % 2][left] = f[(start - 1) % 2][left - nums[start - 1]] + f[(start - 1) % 2][left]
                else:
                    f[start % 2][left] = f[(start - 1) % 2][left]

        return f[n % 2][t]

# 4. 
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n, total = len(nums), sum(nums)
        if (target + total) % 2: return 0
        t = (target + total) // 2
        if t < 0: return 0

        f = [0] * (t + 1)
        f[0] = 1                      
        for start in range(1, n + 1):
            x = nums[start - 1]
            for left in range(t, x - 1, -1): 
                # f[left] = f[left - x] + f[left]
                f[left] += f[left - x]

        return f[t]