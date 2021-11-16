class Solution:
    def sum_chars(self, word: str):
        sum_word = ""
        for i in range(len(word)):
            cur = str(ord(word[i]) - 97)
            sum_word += cur
        return int(sum_word)
    
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        a = self.sum_chars(firstWord)
        b = self.sum_chars(secondWord)
        c = self.sum_chars(targetWord)
        
        return a + b == c
    