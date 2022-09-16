from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        def helper(q):
            stack = []
            num = 0
            sign = "+"
            
            while q:
                c = q.popleft()
                
                if c.isdigit():
                    num = num * 10 + int(c)
                
                if (not c.isdigit() and c != ' ') or not q:
                    if sign == "+":
                        stack.append(num)
                    elif sign == "-":
                        stack.append(-num)
                    elif sign == "*":
                        stack[-1] = stack[-1] * num
                    elif sign == "/":
                        # in python if there is a negative number, we should alway use int() instead of //
                        stack[-1] = int(stack[-1] / num)
                    
                    num = 0
                    sign = c
                    
            return sum(stack)
                
        return helper(deque(s))