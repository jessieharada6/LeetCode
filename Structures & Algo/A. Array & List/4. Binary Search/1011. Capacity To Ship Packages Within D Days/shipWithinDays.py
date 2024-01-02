class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def getDays(m):
            days = 1
            i = 0
            for _ in range(len(weights)):
                cap = m
                while i < len(weights):
                    if cap < weights[i]:
                        days += 1
                        break
                    else:
                        cap -= weights[i]
                    i += 1
                
            return days

        l, r = 0, sum(weights)
        while l + 1 < r:
            m = (l + r) // 2
            if getDays(m) <= days:
                r = m
            else:
                l = m
        return r
        
            
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def getDays(m):
            days = 1
            i = 0

            for _ in range(len(weights)):
                cap = m
                while i < len(weights):
                    if cap < weights[i]:
                        days += 1
                        break
                    else:
                        # try to put as much weight as possible
                        cap -= weights[i]
                    i += 1
                
            return days
        
        
        # l: minimum, r: maximum - possible weight capacity of the ship
        l, r = 0, 0
        for w in weights:
            l = max(w, l)
            r += w
        
        while l < r:
            m = l + floor((r - l) / 2) # ship cap
            if getDays(m) <= days:
                r = m
            else:
                l = m + 1
        return l