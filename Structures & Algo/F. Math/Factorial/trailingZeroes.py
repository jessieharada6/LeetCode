class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0

        while n != 0:
            f = n // 5
            n = f
            count += f
        
        return count