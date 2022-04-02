# follow up - binary search
# Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:             
        def searchIndex(arr, target):
            l = 0
            r = len(arr)
            while l < r:
                m = l + floor((r - l) / 2)
                if arr[m] < target:
                    l = m + 1 # take the next position
                else:
                    r = m
            return l
        
        # t index
        index = collections.defaultdict(list)
        for i, c in enumerate(t):
            index[c].append(i)
            
        # index = {} 
        # for i in range(len(t)):
        #     if t[i] in index:
        #         index[t[i]].append(i)
        #     else:
        #         index[t[i]] = [i]
        # print(index)
        
        j = 0
        for i in range(len(s)):
            c = s[i]
            l = index[c]
            if c not in index:
                return False
            
            #pos = searchIndex(l, j)
            pos = bisect.bisect_left(l, j)
            # print(pos)
            
            if pos == len(l): # pos is out of index - no pos found
                return False 
            
            j = l[pos] + 1 # j increments based on the current index[c][pos] val
            
                    
        return True


# simplified two pointers
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:     
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len(s) 
        

# two pointers
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        
        return True if i == len(s) else False

# queue pop
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        q = list(s)
        
        for c in t:
            if not q: # s is shorter than t
                return True
            
            if c == q[0]:
                q.pop(0)
        
        return not q
            

