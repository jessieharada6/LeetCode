class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : (x[1]))
        n = len(intervals)
        
        prev = intervals[0]
        o = 0
        
        for i in range(1, n):
            curr = intervals[i]
            if prev[1] > curr[0]:
                o += 1
            else:
                prev[1] = curr[1]
        
        return o