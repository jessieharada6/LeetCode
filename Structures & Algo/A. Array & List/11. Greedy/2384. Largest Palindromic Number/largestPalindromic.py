class Solution:
    def largestPalindromic(self, num: str) -> str:
        counter = Counter(num)
        
        if len(num) == counter["0"]:
            return "0"
        
        s = ""
        for d in digits[:0:-1]:
            s += d * (counter[d] // 2)
        if s:
            s += "0" * (counter["0"] // 2)
        
        t = s[::-1]
        
        for d in digits[::-1]:
            if counter[d] % 2:
                s += d
                break
        
        return s + t