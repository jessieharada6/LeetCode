# hashMap via defaultdict to find the difference
# if the value is not the same, thats the extra character
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sMap = defaultdict(int)
        for c in s:
            sMap[c] += 1
        
        tMap = defaultdict(int)
        for c in t:
            tMap[c] += 1
        
        
        for c in t:
            if sMap[c] != tMap[c]:
                return c

# find difference by converting character into integer
# calculate the difference and convert it back to character
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sSum, tSum = 0, 0
        
        for c in s:
            sSum += ord(c)
        
        for c in t:
            tSum += ord(c)
        
        return chr(tSum - sSum)
        