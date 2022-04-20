# 24321 -> 34221

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # convert int to list 
        s = list(str(n))
        n = len(s)
        i = n - 2
        
        # looking for the incrementing part
        while i >= 0:
            if s[i] < s[i + 1]:
                break
            i -= 1
        
        if i == -1:
            return -1
        
        # exchange the next larger element
        for j in range(n - 1, -1, -1):
            if s[i] < s[j]:
                s[i], s[j] = s[j], s[i]
                break
                
        # sort descending
        s[i+1:] = s[i+1:][::-1] # 4221 -> 1224
        
        res = "".join(s)
        return int(res) if int(res) < 2**31 else -1