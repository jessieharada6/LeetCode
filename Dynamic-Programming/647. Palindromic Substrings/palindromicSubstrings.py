class Solution:
    def countSubstrings(self, s: str) -> int:
        # declare as self.count as the property of the class 
        # if not, when calling count += 1 in helper function, 
        #   UnboundLocalError: local variable referenced before assignment
        self.count = 0
        
        def helper(l, r, s):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                self.count += 1
                l -= 1
                r += 1
        
        for i in range(0, len(s)):
            helper(i, i, s)
            helper(i, i + 1, s)
        
        return self.count        

class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count = 0
        
        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                self.count += 1
                l -= 1
                r += 1
        
        for i in range(len(s)):
            helper(i, i)
            helper(i, i + 1)
        
        return self.count