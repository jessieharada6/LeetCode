class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)

        @cache
        def dfs(cur, left): # 给定当前点和剩余fuel返回路径总数
            res = 0

            if abs(locations[cur] - locations[finish]) > left:
                return res

            if cur == finish: 
                res += 1 # reach finish
            
            for i in range(n):
                if cur != i:
                    cost = abs(locations[cur] - locations[i])
                    if cost <= left:
                        res += dfs(i, left - cost) # 从定义出发 返回路径总数 +
            
            return res % (10 ** 9 + 7)
        return dfs(start, fuel) 

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        @cache
        def dfs(i, left): 
            if abs(locations[finish] - locations[i]) > left: #剪枝
                return 0
            
            res = 0
            if i == finish:
                res += 1

            for j in range(n):
                if i != j:
                    cost = abs(locations[j] - locations[i])
                    if cost <= left:
                        res += dfs(j, left - cost)
            return res % (10 ** 9 + 7)
        
        return dfs(start, fuel)