class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : (x[0], -x[1]))
        
        output = 0
        
        # logic:
        # the interval will be at least 1
        # use the starting point to compare
        prev = intervals[0][0]
        
        for _, r in intervals:
            if r > prev:
                output += 1
                # current max ending 
                prev = r
        
        return output


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        output = len(intervals)
        
        # compare based on the ending
        # sort first element ascending
        # if first element is the same, sort second element descending
        intervals.sort(key = lambda x:(x[0], -x[1]))
        # print(intervals)
        
        prev = intervals[0][0]
        
        for _, r in intervals:
            # update current max for r
            if r > prev:
                prev = r
            # logic: found an interval that can be removed
            else:
                output -= 1
        
        return output
        
                