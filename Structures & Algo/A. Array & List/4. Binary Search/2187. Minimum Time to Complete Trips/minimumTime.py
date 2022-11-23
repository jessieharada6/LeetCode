class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l, r = 1, min(time) * totalTrips   # minutes
        
        while l <= r:
            m = (l + r) // 2
            curTrip = self.getCurTrip(time, m)
            if curTrip < totalTrips:
                l = m + 1
            else:
                r = m - 1
        
        return l
    
    def getCurTrip(self, time, curTime):
        total = 0
        for t in time:
            total += curTime // t
        return total
        