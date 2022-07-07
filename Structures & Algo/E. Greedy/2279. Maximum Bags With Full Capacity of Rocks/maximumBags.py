class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        rest = [0 for _ in range(n)]
        for i in range(n):
            rest[i] = capacity[i] - rocks[i]
        
        rest.sort()                

        ans = 0
        for i in range(n):
            additionalRocks -= rest[i]
            if additionalRocks < 0:
                break
            ans += 1
        
        return ans

