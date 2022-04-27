class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def getHours(m):
            hours = 0
            for p in piles:
                hours += ceil(p / m)
            return hours
    
        l = 1 # min is 1 as per constraints
        r = max(piles) # max per hour is the max number in the pile
        while l < r: # exit when l == r at 4
            m = floor(l + (r - l)/2)
            # print(m,  getHours(m))
            if getHours(m) <= h:
                # <: eating too much per hour
                # =: narrow the range so to find the most left number (min)
                r = m
            elif getHours(m) > h:
                # >: eating too little per hour
                l = m + 1
        
        return l

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1           # 1 instead of min(piles) for case of [312884470]: 312884469 hours
        r = max(piles)

        def getHours(num):
            hours = 0
            for p in piles:
                hours += ceil(p / num)
            return hours
        
        while l <= r:
            m = l + (r - l)//2
            if getHours(m) <= h:
                r = m - 1
            else:
                l = m + 1
        
        return l
        
        