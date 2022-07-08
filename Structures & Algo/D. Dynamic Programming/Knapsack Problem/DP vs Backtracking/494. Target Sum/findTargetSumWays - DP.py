class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if (total + target) % 2 or total < abs(target):
            return 0
    
        
        def subsets(nums, total):
            n = len(nums)
            dp = [0] * (total + 1)
            dp[0] = 1
            
            for i in range(1, n + 1):
                for j in range(total, -1, -1):
                    if j - nums[i - 1] >= 0:
                        dp[j] = dp[j] + dp[j - nums[i - 1]]
            
            return dp[total]
        
        return subsets(nums, (total + target) // 2)

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if (total + target) % 2 or total < abs(target):
            return 0
    
        
        def subsets(nums, total):
            n = len(nums)
            dp = [[0] * (total + 1) for _ in range(n + 1)]
        
            dp[0][0] = 1

            for i in range(1, n + 1):
                for j in range(total + 1):
                    if j - nums[i - 1] >= 0:
                        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                    else:
                        dp[i][j] = dp[i - 1][j] 
            
            return dp[n][total]
        
        return subsets(nums, (total + target) // 2)


# [0,0,0,0,0,0,0,0,1]
# 1
    

    
