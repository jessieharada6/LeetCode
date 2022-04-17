class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        output = 0
        stack = []
        
        for b in s:
            if b == "(":
                stack.append(b)
            else:
                if stack != []:
                    stack.pop()
                else:
                    output += 1
        
        return output + len(stack)

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0 # number of insertions
        right = 0 # number of needed right brackets
        
        for b in s:
            if b == "(":
                right += 1 # right needs 1
            else:
                if b == ")":
                    right -= 1 # reduce right
                    if right == -1:
                        right = 0
                        res += 1
        
        return res + right

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left = 0
        right = 0
        
        for b in s:
            if b == "(":
                left += 1
            else:
                if b == ")":
                    left -= 1
                    if left == -1:
                        left = 0
                        right += 1
        
        return left + right