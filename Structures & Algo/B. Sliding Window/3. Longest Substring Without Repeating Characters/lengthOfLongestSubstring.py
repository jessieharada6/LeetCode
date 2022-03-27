class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        have = {}
        
        l = r = 0
        while r < len(s):
            c = s[r]
            r += 1
            have[c] = have.get(c, 0) + 1   
            
            while have[c] > 1:
                d = s[l]
                l += 1
                have[d] -= 1
            
            ans = max(r - l, ans)
        
        return ans