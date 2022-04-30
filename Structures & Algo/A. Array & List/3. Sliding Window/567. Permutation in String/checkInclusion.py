class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = r = 0
        s = {}
        valid = 0
        need = {}
        have = {}
        for c in s1:
            need[c] = need.get(c, 0) + 1
        
        while r < len(s2):
            c = s2[r]
            r += 1
            if c in s1:
                have[c] = have.get(c, 0) + 1
                if have[c] == need[c]:
                    valid += 1

            while valid == len(need):
                if r - l == len(s1):
                    return True
                
                d = s2[l]
                l += 1
                if d in s1:
                    if have[d] == need[d]:
                        valid -= 1
                    have[d] -= 1  
        
        return False