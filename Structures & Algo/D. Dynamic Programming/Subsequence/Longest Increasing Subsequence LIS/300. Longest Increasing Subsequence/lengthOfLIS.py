class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]
        
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        top = [0 for _ in range(n)]
        piles = 0
        
        for i in range(n):
            poker = nums[i]
            
            l = 0
            r = piles
            
            while l < r:
                m = l + (r - l) // 2
                if top[m] < nums[i]:
                    l = m + 1
                else:
                    r = m
            
            if l == piles:
                piles += 1
            top[l] = poker
        
        return piles
                