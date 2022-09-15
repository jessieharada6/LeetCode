class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        s, tank, start = 0, 0, 0
        
        for i in range(n):
            s += gas[i] - cost[i]  
        if s < 0: return -1
        
        for i in range(n):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0

        return 0 if start == n else start
        
            

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        s = 0
        min_sum = 0
        start = 0
        
        for i in range(n):
            s += gas[i] - cost[i]
            if s < min_sum:
                start = i + 1
                min_sum = s
        
        if s < 0: return -1
        return 0 if start == n else start
        

