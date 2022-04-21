class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        
        for b in s:
            if b in map: 
                stack.append(b)
            else:
                if len(stack) == 0 or map[stack.pop()] != b:
                    return False
        
        return len(stack) == 0


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        
        for b in s:
            if b in map: # key in map
                stack.append(b)
            else:
                if len(stack) != 0 and map[stack[-1]] == b:
                        stack.pop(-1) # pop last element
                else:
                    return False
        
        return len(stack) == 0