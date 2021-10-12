class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        output = 0
        left = right = 0
        numT = numF = 0
        n = len(answerKey)
        
        while right < n:
            # slide window to the right
            if answerKey[right] == "T":
                numT += 1
            else:
                numF += 1
                
            # while numT and numF > k
            # meaning we can't change the T and F anymore
            # slide left
            while numT > k and numF > k:
                if answerKey[left] == "T":
                    numT -= 1
                else:
                    numF -= 1
                left += 1
            
            # calculate output
            output = max(output, right - left + 1)
            right += 1
        
        return output
        