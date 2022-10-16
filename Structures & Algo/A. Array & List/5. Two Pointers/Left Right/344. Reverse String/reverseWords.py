class Solution:
    def reverseWords(self, s: str) -> str:
        s = self.remove_space(s)
        s_list = list(s)
        s_list = self.reverse_string(s_list)
        s_list = self.reverse_word(s_list)
        return ''.join(s_list)
    
    def remove_space(self, s):
        l, r = 0, len(s) - 1
        while l < r and s[l] == " ":
            l += 1
        while l < r and s[r] == " ":
            r -= 1
        new_s = ''
        while l <= r:
            if s[l] != ' ':
                new_s += s[l]
            elif s[l] == ' ' and new_s[-1] != ' ':
                new_s += s[l]
            l += 1
        return new_s
        
    def reverse_string(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return s
    
    def reverse_word(self, s):
        l, r = 0, 0
        while r < len(s):
            while r < len(s) and s[r] != ' ':
                r += 1
            s[l:r] = self.reverse_string(s[l:r])
            l = r + 1
            r += 1
        return s
            
                