class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 1, max(candies)          # number of candies
        while l <= r:
            m = (l + r) // 2
            curChildren = self.getChildren(candies, m)  
            # max, right bound
            if curChildren >= k:
                l = m + 1
            else:
                r = m - 1
                
        return r
    
    def getChildren(self, candies, curCandies):
        total = 0
        for c in candies:
            total += c // curCandies
        return total