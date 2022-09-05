class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : (x[0]))
        
        n = len(intervals)
        res = [intervals[0]]
        
        for i in range(1, n):
            cur = intervals[i]
            prev = res[-1]
            
            if prev[1] >= cur[0]:
                prev[1] = max(prev[1], cur[1])
            else:
                res.append(cur)
        
        return res