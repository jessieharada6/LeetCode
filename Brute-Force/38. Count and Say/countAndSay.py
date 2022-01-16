class Solution:
    def countAndSay(self, n: int) -> str:
        say = "1"
        
        for i in range(n - 1):
            current = say[0]
            count = 0
            temp = ""
            
            for c in say:
                if c == current:
                    count += 1
                else:
                    # append current result
                    # e.g. 111 => "31", 2 => "12"
                    temp += str(count) + current
                    # move to the next result
                    count = 1
                    current = c
            
            # append the final part of the result
            temp += str(count) + current
            say = temp
        
        return say