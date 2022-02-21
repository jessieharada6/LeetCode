class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : (x[0], -x[1]))
        
        output = 0
        
        # logic:
        # the interval will be at least 1
        # use the -1 as the starting point to compare
        # as long as right point > current right point, a new interval is needed

        # as element value starts from 0
        prev = -1
        
        for _, r in intervals:
            if r > prev:
                output += 1
                # current max ending 
                prev = r
        
        return output


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        output = len(intervals)
        
        # sort first element ascending
        # if the first element is the same, sort the second element descending
        intervals.sort(key = lambda x:(x[0], -x[1]))
        # print(intervals)
        
        prev = -1
        
        for _, r in intervals:
            # update current max for r
            if r > prev:
                prev = r
            # logic: found an interval that can be removed
            else:
                output -= 1
        
        return output
        
                