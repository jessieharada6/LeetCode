class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # 在k长度里 最多有多少vowel
        # 如果当前字符是元音 予以记录
        # 当 r - l + 1 > k 时 l += 1 并减去对应的元音
        # 把count计入ans里 算max
        
        vowel = ['a', 'e', 'i', 'o', 'u']
        
        l = 0
        ans = 0
        count = 0
        for r, c in enumerate(s):
            if c in vowel:
                count += 1
            
            while r - l + 1 > k:
                if s[l] in vowel:
                    count -= 1
                l += 1
            
            ans = max(ans, count)
  

        return ans