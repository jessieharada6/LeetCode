# O(n)
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            arr = [int(n) for n in str(num)]
            num = sum(arr)
        
        return num


# O(1)
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        
        return 9 if num % 9 == 0 else num % 9