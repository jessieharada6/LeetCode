class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # print(ord("A"))
        # print(chr(65))
        
        sum = 0
        for i, val in enumerate(columnTitle):
            sum += (ord(val) - 64) * pow(26, len(columnTitle) - 1 - i)
        
        return sum