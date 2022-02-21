# logic
# sort both elements in asending order
# compare output's last element's right point to the next left point in intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x : (x[0], x[1]))
        output = [[intervals[0][0], intervals[0][1]]]
        
        
        for i in range(1, len(intervals)):
            if output[-1][1] >= intervals[i][0]:
                # update existing output element
                output[-1][1] = max(output[-1][1], intervals[i][1])
            else:
                # add a new output element, this becomes the last element in the output
                output.append([intervals[i][0], intervals[i][1]])
            
        return output
                


class Solution:   
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        
        # sort the first element
        intervals.sort()
        output.append(intervals[0])
        # print(intervals)
        
        # check the overlap
        for i in range(1, len(intervals)):
            if output[-1][1] >= intervals[i][0]:
                output[-1][1] = max(output[-1][1], intervals[i][1])
            else:
                output.append(intervals[i])
        
        return output

class Solution:   
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nlogn), logn is the built-in sorting method
        # sort starting value
        intervals.sort(key = lambda i : i[0])
        
        output = [intervals[0]]
        
        for start, end in intervals[1:]:
            last_end = output[-1][1]
            
            if start <= last_end:
                output[-1][1] = max(output[-1][1], end)
            else:
                output.append([start, end])
        
        
        return output
        