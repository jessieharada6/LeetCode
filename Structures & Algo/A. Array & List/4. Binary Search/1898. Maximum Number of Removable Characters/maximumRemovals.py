class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        k = 0
        sArr = list(s)
        l, r = 0, len(removable)
       
        while l <= r:
            m = (l + r) // 2
            for i in range(m):
                sArr[removable[i]] = 0
            isTrue = self.isSubsequence(sArr, p)
            if isTrue:
                l = m + 1
            else:
                for i in range(l, m):
                    sArr[removable[i]] = s[removable[i]]
                r = m - 1

        return r
    
    def isSubsequence(self, s, p):
        i, j = 0, 0
        while i < len(s) and j < len(p):
            if s[i] == p[j]:
                j += 1
            i += 1
        
        if j == len(p):
            return True
        return False