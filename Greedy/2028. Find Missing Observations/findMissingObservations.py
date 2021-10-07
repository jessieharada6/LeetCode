class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        diff = (m + n) * mean - sum(rolls)
        
        if diff > n * 6 or diff < n:
            return []
        
        output = [floor(diff/n) for _ in range(n)]
        remaining = diff % n
        print(output)
        
        for i in range(remaining):
            output[i] += 1
        
        return output