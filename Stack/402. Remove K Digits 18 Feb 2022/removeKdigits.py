class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # remove digits without changing order
        # the removed part does not need to be contiguous
        
        # A. make the list as ascending (e.g 1139)
        # a < b
        # abc
        # ab > bc, ac > bc
        # a is the largest, remove a
        
        # B. then remove the ascending part from the end
        # a < b < c
        # c is the largest, remove c
        
        stack = []
        
        for n in num:
            # A. remove slope (any num that forms descending shape e.g. 4321)
            while stack and k and int(stack[-1]) > int(n):
                # pop from right side
                stack.pop()
                k -= 1
            stack.append(n)
        
        #B. uphill - use any remaining k to remove the tips
        for i in range(k):
            stack.pop()
        
        # remove all 0 from left side 
        # and if the stack is empty, return "0"
        return "".join(stack).lstrip("0") or "0"