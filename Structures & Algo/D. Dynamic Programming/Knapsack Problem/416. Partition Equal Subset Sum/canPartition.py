class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total, mod = divmod(sum(nums), 2)
        if mod: return False
        
        n = len(nums)
        dp = [[False] * (total + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = True
        
        for i in range(1, n + 1):
            for j in range(1, total + 1):
                if j - nums[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[n][total]

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total, mod = divmod(sum(nums), 2)
        if mod: return False
        
        n = len(nums)
        dp = [False] * (total + 1)
        
        dp[0] = True
        
        for i in range(1, n + 1):
            for j in range(total, 0, -1):  ### 
                if j - nums[i - 1] >= 0:
                    dp[j] = dp[j] or dp[j - nums[i - 1]]
        
        return dp[total]