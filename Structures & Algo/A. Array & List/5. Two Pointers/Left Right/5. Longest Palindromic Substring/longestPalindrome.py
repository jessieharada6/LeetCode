class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindromes(s, l, r):
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]
        
        res = ""
        for i in range(len(s)):
            s1 = palindromes(s, i, i)
            s2 = palindromes(s, i, i + 1)
            print(s1, s2)
            res = s1 if len(res) < len(s1) else res
            res = s2 if len(res) < len(s2) else res
        
        return res