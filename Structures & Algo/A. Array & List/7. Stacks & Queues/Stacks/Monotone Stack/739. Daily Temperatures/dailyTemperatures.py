class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        s = []
        res = [0 for _ in range(n)]
        
        for i in range(n - 1, - 1, -1):
            while s and temperatures[s[-1]] <= temperatures[i]: # use t to decide whether to pop
                s.pop()
            res[i] = s[-1] - i if s else 0 # record the index diff to get distance
            s.append(i)
        
        return res