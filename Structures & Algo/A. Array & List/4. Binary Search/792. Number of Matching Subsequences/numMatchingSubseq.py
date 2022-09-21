class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        res = 0
        
        pos = defaultdict(list)
        for i, c in enumerate(s):
            pos[c].append(i)
        
        for word in words:
            print(word)
            i, j = 0, 0
            for w in word:
                indexes = pos[w]
                if not indexes: break # no such char
                
                cur = self.left_bound(indexes, j) # indexes' index
                if cur == -1: break   # no more char left
                j = indexes[cur] + 1  # j moves to the next index - ready for the next time
                i += 1
            
            if i == len(word):
                res += 1
        
        return res
    
    def left_bound(self, arr, target):
        l, r = 0, len(arr)
        while l < r:
            m = l + (r - l) // 2
            if arr[m] < target:
                l = m + 1
            else:
                r = m
        
        if l == len(arr):
            l = -1
        
        return l
        
                