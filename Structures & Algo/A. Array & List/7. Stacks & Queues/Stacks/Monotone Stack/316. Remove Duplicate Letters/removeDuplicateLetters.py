class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        inStack = [False for _ in range(256)]
        count = [0 for _ in range(256)] # ascii
        stack = []
        
        sList = list(s)
        for c in sList:
            count[ord(c)] += 1
        
        for c in sList:
            num = ord(c)
            # update the count b/f checking inStack is True, otherwise it wont deduct the count
            count[num] -= 1 
                      
            if inStack[num]:
                continue
            
            while stack and stack[-1] > c: # dictionary order (the smallest in lexicographical order)
                if count[ord(stack[-1])] == 0:
                    break
                inStack[ord(stack.pop())] = False
                    
            stack.append(c)
            inStack[num] = True
        
        return "".join(stack)