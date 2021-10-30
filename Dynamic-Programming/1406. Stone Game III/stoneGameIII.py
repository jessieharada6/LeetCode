class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        
        # 1.
        # use suffix sum, as initially, the stoneValue is the max
        # then it get less and less as players play
        suffix_sum = [0] * (n - 1) + [stoneValue[-1]]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] += suffix_sum[i + 1] + stoneValue[i]
        
        # 2.
        # dp - each index shows (alice - bob) best score
        # dp - create one more element so that if there's no stone, it shows 0 tie
        dp = [0] * n + [0]
        for i in range(n - 1, -1, -1):
            # when it's reaching 3, we must let go of one, and we choose the lowest value 
            dp[i] = suffix_sum[i] - min(dp[i + 1 : i + 4])
        
        # 3.
        # compare, to win, alice must have more than half of the stones in comp to the sum
        total = sum(stoneValue)
        if dp[0] * 2 == total:
            return "Tie"
        elif dp[0] * 2 > total:
            return "Alice"
        else:
            return "Bob"
        