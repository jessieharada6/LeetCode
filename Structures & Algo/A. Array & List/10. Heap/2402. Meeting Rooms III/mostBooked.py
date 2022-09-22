class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        res = 0
        
        meetings.sort() 
        
        idle = list(range(n)) # [i for i in range(n)]
        using = [] 
        cnt = [0] * n
        
        for st, end in meetings:
            while using and using[0][0] <= st:
                heappush(idle, heappop(using)[1])
            if len(idle) == 0:
                e, i = heappop(using)
                end += e - st
            else:
                i = heappop(idle)
            
            cnt[i] += 1
            heappush(using, (end, i))
        
        ans = 0
        for i, c in enumerate(cnt):
            if c > cnt[ans]:
                ans = i
        
        return ans
        