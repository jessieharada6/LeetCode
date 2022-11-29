class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        n = len(removable)
        l, r = 0, n - 1
        
        while l <= r:
            m = (l + r) // 2
            isTrue = self.isSubsequence(removable, m, s, p)
            if isTrue:
                l = m + 1
            else:
                r = m - 1
        return l
    
    def isSubsequence(self, removable, m, s, p):
        i, j, n = 0, 0, len(p)
        pos = set()
        for k in range(m + 1):
            pos.add(removable[k])
        
        while i < len(s) and j < n:
            if i not in pos and s[i] == p[j]:
                j += 1
            i += 1
        
        return j == n

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        n = len(removable)
        sList = list(s)
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            sList = self.updateList(sList, removable, m)
            isTrue = self.isSubsequence(sList, p)
            if isTrue:
                l = m + 1
            else:
                sList = self.recoverList(s, sList, removable, m)
                r = m - 1
        return l
    
    def updateList(self, sList, removable, m):
        for i in range(m + 1):
            sList[removable[i]] = 0
        return sList
    
    def isSubsequence(self, sList, p):
        i, j = 0, 0
        while i < len(sList) and j < len(p):
            if sList[i] == p[j]:
                j += 1
            i += 1

        if j == len(p):
            return True
        return False
    
    def recoverList(self, s, sList, removable, m):
        for i in range(m + 1):
            sList[removable[i]] = s[removable[i]]
        return sList
    