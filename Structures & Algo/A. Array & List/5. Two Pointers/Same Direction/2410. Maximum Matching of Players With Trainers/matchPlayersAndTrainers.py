class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # p <= t 只能匹配一个 
        # sort
        # 双指针 一个指player 一个指t
        # if p > t: t += 1 不匹配 向右走
        # else: ans += 1 p += 1 t += 1 找到一个配对
        
        players.sort()
        trainers.sort()
        p = t = ans = 0

        while True:

            if p >= len(players) or t >= len(trainers):
                break
                
            if players[p] > trainers[t]:
                t += 1
            else:
                ans += 1
                p += 1
                t += 1
            
        
        return ans


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
            