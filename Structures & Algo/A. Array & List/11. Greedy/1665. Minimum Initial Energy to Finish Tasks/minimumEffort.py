class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[0] - x[1])
        
        p = cur = 0
        for a, m in tasks:
            p = max(p, cur + m)
            cur += a
        return p
        
