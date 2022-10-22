class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 用字典存下标
        # l起始-1
        # 当c存在于字典里 l移到储存着的c的下标的位置 
        # 且必须是l < 下标时候 l不可倒退 （举例：abba)
        
        l = -1
        ans = 0
        d = {}
        for r, c in enumerate(s):
            if c in d and l < d[c]:
                l = d[c]
            
            ans = max(ans, r - l)

            d[c] = r
            
            
        return ans
        