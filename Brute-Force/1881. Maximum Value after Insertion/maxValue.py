class Solution:
    def maxValue(self, n: str, x: int) -> str:
        
        # positive
        if n[0] != "-":
            new_str = ""
            is_x_added = False
            
            # add x only if x > n[i]
            for i in range(len(n)):
                if x > int(n[i]):
                    # form a new string, without concat
                    new_str = n[:i] + str(x) + n[i:]
                    is_x_added = True
                    break
                else:
                    new_str += n[i]
            if not is_x_added:
                new_str += str(x)
        
        # negative
        else:
            new_str = ""
            is_x_added = False
            n = n[1:]
            
            for i in range(len(n)):
                if x < int(n[i]):
                    new_str = n[:i] + str(x) + n[i:]
                    is_x_added = True
                    break
                else:
                    new_str += n[i]
            if not is_x_added:
                new_str += str(x)
            new_str = "-" + new_str
        
        return new_str
