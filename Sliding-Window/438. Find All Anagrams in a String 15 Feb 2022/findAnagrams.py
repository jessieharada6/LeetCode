class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        output = []
        
        if len(s) < len(p):
            return output
        
        pMap = {}
        sMap = {}
        
        # init sliding window by hashMaps
        for i in range(len(p)):
            pMap[p[i]] = pMap.get(p[i], 0) + 1
            sMap[s[i]] = sMap.get(s[i], 0) + 1
        
        # compare initial maps 
        output.append(0) if pMap == sMap else []
        
        # two pointers to slide window
        l = 0 
        r = len(p) # r starting at the updating point
        while r <len(s):
            sMap[s[r]] = sMap.get(s[r], 0) + 1
            sMap[s[l]] -= 1
            if sMap[s[l]] == 0:
                sMap.pop(s[l])
            l += 1
            r += 1
            
            if sMap == pMap:
                output.append(l)
                
        return output