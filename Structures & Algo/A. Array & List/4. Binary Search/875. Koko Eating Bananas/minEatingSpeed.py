from math import ceil
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int: 
        l, r = 0, max(piles)
        while l + 1 < r:
            m = (l + r) // 2
            hours = self.getHours(piles, m)
            print(m, hours)
            if hours <= h:
                r = m # r is always the correct one
            else:
                l = m
        return r
    
    def getHours(self, piles, curBanana):
        total = 0
        for p in piles:
            total += (p + curBanana - 1) // curBanana
        return total

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles.length <= h <= 10^9 -- can definitely finish all piles 
        l, r = 1, max(piles)   # bananas/hour, max(piles) -> len(piles) hours finish
        while l <= r:
            m = (l + r) // 2
            hours = self.getHours(piles, m)
            if hours <= h:
                r = m - 1
            else:
                l = m + 1
        return l
    
    def getHours(self, piles, curBanana):
        total = 0
        for p in piles:
            total += (p + curBanana - 1) // curBanana
        return total
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
        
        