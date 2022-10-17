class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        day = 0
        last = Counter()
        for t in tasks:
            day += 1
            if t in last:
                day = max(day, last[t] + space + 1)
            last[t] = day
        
        return day