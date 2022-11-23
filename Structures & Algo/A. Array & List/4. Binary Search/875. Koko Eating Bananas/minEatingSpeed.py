from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)         # bananas
        while l <= r:
            m = (l + r) // 2
            hours = self.getHours(piles, m)
            # print(hours, l, m, r)
            if hours <= h:
                r = m - 1
            else:
                l = m + 1
        
        return l
    
    
    def getHours(self, piles, curBanana):
        total = 0
        for p in piles:
            total += ceil(p / curBanana)
        return total

# m = floor(l + (r - l)/2)
        
        