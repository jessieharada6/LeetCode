class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        have = {}
        need = {}
        for c in p:
            need[c] = need.get(c, 0) + 1
        
        l = r = 0
        valid = 0
        while r < len(s):
            c = s[r]
            r += 1
            if c in need:
                have[c] = have.get(c, 0) + 1
                if need[c] == have[c]:
                    valid += 1
            
            if r - l == len(p):
                if valid == len(need):
                    ans.append(l)
                
                d = s[l]
                l += 1
                if d in need:
                    if need[d] == have[d]:
                        valid -= 1
                    have[d] -= 1
        
        return ans