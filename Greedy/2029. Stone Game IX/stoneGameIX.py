class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        count = [0] * 3
        for s in stones:
            count[s % 3] += 1
        
        # Alice wins in the below situations
        if count[0] % 2 == 0 and count[1] * count[2] > 0:
            return True
        if count[0] % 2 == 1 and abs(count[1] - count[2]) >= 3:
            return True
        return False 