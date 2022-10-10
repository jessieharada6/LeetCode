class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        # 4, 7, 9
        # 2, 5, 8, 8
        
        j, m = 0, len(trainers)
        
        for i, p in enumerate(players):
            print(i, j)
            while j < m and p > trainers[j]:    # check j < m first otherwise index out of list
                j += 1
            
            if j == m:      
                return i
            
            j += 1          # check j == m first
            
        return len(players)
            