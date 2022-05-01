import random
class Solution:
    # hashmap to represent reflected value 
    # to simulate pushing elements to the end (to enhance intimacy of group of elements)
    def __init__(self, n: int, blacklist: List[int]):
        # [0, self.white - 1] is whitelist, [white, n - 1] is blacklist
        self.white = n - len(blacklist)
        self.dict = {}
        last = n - 1

        for b in blacklist:
            self.dict[b] = -1                       # mark blacklist
        
        for b in blacklist:
            if b >= self.white:                     # in the range of blacklist, leave it, as we won't pick a rand in the range of blacklist
                continue
            
            while last in self.dict:                # last is in blacklist
                last -= 1                           # reduce last so the element won't repeat

            self.dict[b] = last                     # reflect blacklist to the white
            last -= 1                               # reduce last so the element won't repeat

    def pick(self) -> int:
        rand = random.randint(0, self.white - 1)    # only pick in the range of [0, self.white - 1]
        if rand in self.dict:
            return self.dict[rand]                  # return the reflected value
        return rand


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()