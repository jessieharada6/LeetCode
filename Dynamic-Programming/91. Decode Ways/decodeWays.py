class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1
        
        for i in range(2, len(dp)):
            option1 = s[i-1:i]
            option2 = s[i-2:i]
            if 1 <= int(option1) <= 9:
                dp[i] += dp[i - 1]
            if 10 <= int(option2) <= 26:
                dp[i] += dp[i - 2]
            
        return dp[-1]

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else dp[0]
        
        for i in range(2, len(dp)):
            option1 = s[i - 1: i]
            option2 = s[i - 2: i]
            if 1 <= int(option1) <= 9:
                dp[i] += dp[i - 1]
            if 10 <= int(option2) <= 26:
                dp[i] += dp[i - 2]
        
        print(dp)
        return dp[-1]