from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        
        def helper(q):
            num = 0
            sign = "+"
            stack = []
            
            while len(q) > 0:
                c = q.popleft()
                
                if c.isdigit():
                    num = 10 * num + int(c)
                
                if c == "(":
                    num = helper(q)
                
                if (not c.isdigit() and c != ' ') or len(q) == 0:
                    if sign == "+":
                        stack.append(num)
                    elif sign == "-":
                        stack.append(-num)
                    num = 0
                    sign = c
                
                if c == ")":
                    break
                
            return sum(stack)
        
        # queue = deque(s.replace(' ',''))
        return helper(deque(s))