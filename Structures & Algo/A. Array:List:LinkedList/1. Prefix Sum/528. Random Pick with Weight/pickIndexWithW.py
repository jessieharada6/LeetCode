import bisect
import random

class Solution:

    def __init__(self, w: List[int]):
        self.prefix = [w[0]]
        for num in w[1 : ]:
            self.prefix.append(self.prefix[-1] + num)
            
    def pickIndex(self) -> int:
        # self.prefix must be sorted in order to use bisect
        # the random number is inserted at the most left position 
        # return index of the random number if being inserted
        index = bisect.bisect_left(self.prefix, random.random() * self.prefix[-1])

        return index
        
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()