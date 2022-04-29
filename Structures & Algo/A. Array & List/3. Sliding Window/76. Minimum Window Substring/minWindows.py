class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = {}
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        
        l = r = 0
        valid = 0
        start = 0
        length = inf
        
        while r < len(s):
            c = s[r] 
            r += 1
            if c in need:
                have[c] = have.get(c, 0) + 1
                if need[c] == have[c]:
                    valid += 1
            
            while valid == len(need): 
                if r - l < length:
                    length = r - l
                    start = l      

                d = s[l]
                l += 1
                
                if d in need:
                    if need[d] == have[d]:
                        valid -= 1
                    have[d] -= 1
        
        return s[start:start + length] if length != inf else ""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = {}
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        
        # pointers
        left = right = 0
        # len(need) == valid meaning we have found all chars in the subarray
        valid = 0 
        # record range
        start = 0
        size = inf
        
        ## sliding
        while right < len(s): # use while instead of if, to minimise the range when it is valid
            # slide right
            c = s[right]
            right += 1
            
            # update valid
            if c in need:
                have[c] = have.get(c, 0) + 1
                if need[c] == have[c]:
                    valid += 1
            
            ## find valid
            while valid == len(need):
                # update pointers and find the size
                if right - left < size:
                    start = left
                    size = right - left
                
                # slide left
                d = s[left]
                left += 1
                
                # update valid
                if d in need:
                    if need[d] == have[d]:
                        valid -= 1
                    have[d] -= 1
                    
        return "" if size == inf else s[start : start + size]
            
            