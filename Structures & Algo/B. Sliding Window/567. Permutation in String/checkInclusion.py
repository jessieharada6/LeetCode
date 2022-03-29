class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {}
        have = {}
        for c in s1:
            need[c] = need.get(c, 0) + 1
            
        l = r = 0
        valid = 0
        while r < len(s2):
            c = s2[r]
            r += 1
            if c in need:
                have[c] = have.get(c, 0) + 1
                if have[c] == need[c]:
                    valid += 1
            
            # substring - the len of the window must be the same as the len of s1
            if r - l == len(s1):
                if valid == len(need):
                    return True
                
                d = s2[l]
                l += 1
                if d in have:
                    if have[d] == need[d]:
                        valid -= 1
                    have[d] -= 1
        return False
                    