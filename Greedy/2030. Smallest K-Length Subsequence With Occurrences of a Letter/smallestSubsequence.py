class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        count = s.count(letter)
        n = len(s)
        stack = []
        
        for index, char in enumerate(s):
            # char < stack[-1] -> select the smaller letter
            # n - index -> remaining length
            # k - len(stack) < repetition: not enough space to fill out repetition
            while stack and ((char < stack[-1] and len(stack) + n - index > k and (stack[-1] != letter or count > repetition)) or k - len(stack) < repetition):
                # pop
                cur = stack.pop()
                if cur == letter:
                    repetition += 1
            
            if len(stack) < k:
                stack.append(char)
                if char == letter:
                    repetition -= 1
            
            if char == letter:
                count -= 1
        
        return "".join(stack)
        