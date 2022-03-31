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