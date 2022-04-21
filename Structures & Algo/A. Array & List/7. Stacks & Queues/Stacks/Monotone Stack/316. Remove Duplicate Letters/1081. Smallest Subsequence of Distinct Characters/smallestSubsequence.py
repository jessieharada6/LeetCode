class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        inStack = [False for _ in range(256)] # ascii
        count = [0 for _ in range(256)]
        
        for c in list(s):
            count[ord(c)] += 1
        
        for c in s:
            current = ord(c)
            count[current] -= 1
            
            if inStack[current]:
                continue
            
            while stack and stack[-1] > c:
                if count[ord(stack[-1])] == 0:
                    break
                inStack[ord(stack.pop())] = False
            
            stack.append(c)
            inStack[current] = True
        
        return "".join(stack)
        