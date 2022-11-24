class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # 方法一
        # 以trainers为主 因为1对1 最长就是min(len(players), len(trainers))本身的长度
        # 排序 原因：用最小的trainer值与当前player匹配 这样才可以有max length
        
        players.sort()
        trainers.sort()
        
        j = 0
        for i, t in enumerate(trainers):
            if j < len(players) and players[j] <= t:
                j += 1
            
        return j 

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 用l,r控制范围
        # r 向右走 当s-nums[l]>=target时 
        
        ans = inf
        s = l = r = 0
        
        for r, x in enumerate(nums):
            s += x
            
            while s - nums[l] >= target: # 事先检查 不做无用功
                s -= nums[l]
                l += 1

            if s >= target:
                ans = min(ans, r - l + 1)
        
        return ans if ans != inf else 0


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # 方法二
        # 同时比较两个 找到match就加入ans
        
        players.sort()
        trainers.sort()
        
        i, j = 0, 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                i += 1
                j += 1
            else: 
                j += 1
        
        return i


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
            