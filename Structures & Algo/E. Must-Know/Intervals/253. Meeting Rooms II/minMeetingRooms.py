def minMeetingRooms(self, meetings: List[List[int]]) -> int:
    n = len(meetings) 
    begin = [0] * n
    end = [0] * n
    for i in range(n):
        begin[i] = meetings[i][0]
        end[i] = meetings[i][1]
    
    begin.sort()
    end.sort()

    count = 0
    res, i, j = 0, 0, 0
    while i < n and j < n:
        if begin[i] < end[j]:
            count += 1
            i += 1
        else:
            count -= 1
            i -= 1
        res = max(res, count)
    
    return res