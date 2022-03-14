class Solution:
    def isValid(self, s: str) -> bool:
        # use stack to preserve order
        stack = []
        map = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        
        for c in s:
            if c in map:
                stack.append(c)
            else:
                if stack == [] or c != map[stack.pop()]:
                    return False
        
        return stack == []