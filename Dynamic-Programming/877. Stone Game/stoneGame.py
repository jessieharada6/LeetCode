class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def get_max(piles):
            max_index = 0
            max_num = 0
            for i in range(len(piles)):
                #tail or head
                if i == 0 or i == len(piles) - 1:
                    max_num = max(piles)
                    max_index = piles.index(max_num)
            return [max_num, max_index]
        
        alice = 0
        bob = 0
        while len(piles):    
            alice += get_max(piles)[0]
            piles.pop(get_max(piles)[1])
            bob += get_max(piles)[0]
            piles.pop(get_max(piles)[1])
            
        
        return alice > bob
            
                