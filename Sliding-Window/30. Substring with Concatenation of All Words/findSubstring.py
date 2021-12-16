class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words[0]) 
        count = {}
        output = []
        
        # build dictionary
        for word in words:
            count[word] = count.get(word, 0) + 1
        
        for i in range(n):
            window = {}
            # l is the starting index * 
            l = r = i
            
            while r < len(s):
                #substring
                current = s[r : r + n]
                
                if current in count:
                    window[current]  = window.get(current, 0) + 1
                    
                    if window[current] <= count[current]:
                        # r starting at a new character to check the new word
                        r += n
                    else:
                        while l <= r and window[current] > count[current]:
                            # spit out the initial word 
                            w = s[l : l + n]
                            # remove the initial word
                            window[w] -= 1
                            # l moves to the new index (new starting index *)
                            l += n
                        # r moves to the new check point
                        r += n
                        
                    if window == count:
                        output.append(l)
                else:
                    window.clear()
                    # slide to the new character
                    # atm, l = r
                    r += n
                    l = r
            
        return output