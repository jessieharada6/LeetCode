# this approach is not so good
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dict = {}
        l = r = 0
        
        # sliding window
        while r < len(s):
            r += 1
            # get the value when it is length of 10
            # add to dict
            if r - l == 10:
                if s[l : r] in dict:
                    dict[s[l : r]] += 1
                else:
                    dict[s[l : r]] = 1
            
            if r - l > 10:
                l += 1
                r -= 1
            
        
        # print(dict)
        # if freq appears to be 2 times or more, then those are repeated dna sequences
        output = [dna for dna, freq in dict.items() if freq >= 2]
        return output

# approach 2
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dict = {}
        l = 0
        
        while l + 9 < len(s):
            # use l + 10, as it is [start, end - 1]
            if s[l : l + 10] in dict:
                dict[s[l : l + 10]] += 1
            else:
                dict[s[l : l + 10]] = 1
            
            l += 1
            
        output = [dna for dna, freq in dict.items() if freq >= 2]
        return output
                