class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0 for _ in range(n + 1)]
        offset = 1
        
        for i in range(1, len(dp)):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        
        return dp
        
        
class Solution:
    def countBits(self, n: int) -> List[int]:
        # another way of initiating the array 
        dp = [0] * (n + 1)
        offset = 1
        print(dp)
        
        for i in range(1, len(dp)):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        
        return dp