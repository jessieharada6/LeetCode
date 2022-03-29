class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = {}
        ans = 0
        
        l = r = 0
        while r < len(s):
            c = s[r]
            r += 1 
            sub[c] = sub.get(c, 0) + 1
            
            while sub[c] > 1:
                d = s[l]
                l += 1
                sub[d] -= 1

            ans = max(r - l, ans)
        
        return ans