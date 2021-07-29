class Solution:
    # n^3
    def minCost(self, n: int, cuts: List[int]) -> int:
        def dp (start, end):
            if (start, end) in memo:
                return memo[(start, end)]
        
            # set ans to infinite           
            ans = sys.maxsize
            # base case
            canCut = False
            
            for cut in cuts:
                if start < cut < end:
                    canCut = True
                    # cost: end - start
                    ans = min(ans, dp(start, cut) + dp(cut, end) + end - start)
            
            if not canCut:
                # if to save the result, 
                # so next time it will return directly from memo
                # use ans = 0 
                return 0
            
            # dict[key]
            memo[(start, end)] = ans

            return ans
            
        memo = {}

        return dp(0, n)