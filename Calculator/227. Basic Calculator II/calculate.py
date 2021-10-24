class Solution:
    def calculate(self, s: str) -> int:
        output = 0
        num = 0
        # need it to be + so can push the first number to the stack
        sign = "+"
        stack = []
        n = len(s)
        
        for i in range(n):
            # if this element is a digit
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            # separated by some number of spaces
            if (not s[i].isdigit() and not s[i].isspace()) or i == n - 1:
                if sign == "+":
                    stack.append(num)
                    print("++", num, stack, i)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    stack.append(math.trunc(stack.pop() / num))
                num = 0
                sign = s[i]
        
        return sum(stack)

class Solution:
    def calculate(self, s: str) -> int:
        output = 0
        number = 0
        sign = "+"
        stack = []
        n = len(s)
        
        for i in range(n):
            if s[i].isdigit():
                number = number * 10 + int(s[i])
            
            if not s[i].isdigit() and not s[i].isspace() or i == n - 1:
                if sign == "+":
                    stack.append(number)
                elif sign == "-":
                    stack.append(-number)
                elif sign == "*":
                    stack.append(stack.pop() * number)
                elif sign == "/":
                    stack.append(trunc(stack.pop() / number))
                sign = s[i]
                number = 0
        
        return sum(stack)
        