class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : (x[0], -x[1]))
        n = len(intervals)
        o = 0
        
        l = intervals[0][0]
        r = intervals[0][1]
        
        for i in range(1, n):
            intv = intervals[i]
            if l <= intv[0] and r >= intv[1]:
                o += 1
            elif r >= intv[0] and r <= intv[1]:
                r = intv[1]
            elif r < intv[0]:
                l = intv[0]
                r = intv[1]
        
        return n - o