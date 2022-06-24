class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        need = 0
        insertions = 0
        
        for c in s:
            if c == "(":
                need += 1
            else:
                need -= 1
                if need == -1:
                    need = 0
                    insertions += 1
        return need + insertions

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        output = 0  # needs of )
        stack = []  # numbers of (
        
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
