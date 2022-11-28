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
    