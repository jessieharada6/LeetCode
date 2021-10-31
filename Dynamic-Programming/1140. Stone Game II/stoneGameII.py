class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        # at each M, for diff number of piles
        dp = [[0 for _ in range(n + 1)] for _ in range(n)]
        sum = 0
        
        for i in range(n - 1, -1, -1):
            sum += piles[i]
            for M in range(1, n + 1, 1):
                if i + 2 * M >= n:
                    # if can select all piles
                    # get all piles
                    dp[i][M] = sum
                else:
                    for x in range(1, 2 * M + 1, 1):
                        #print(sum, i, x, M)
                        # within this range of [1, 2M]
                        # pick the smallest pile so that the current value is optimal
                        dp[i][M] = max(dp[i][M], sum - dp[i + x][max(x, M)])
        
        return dp[0][1]
                

