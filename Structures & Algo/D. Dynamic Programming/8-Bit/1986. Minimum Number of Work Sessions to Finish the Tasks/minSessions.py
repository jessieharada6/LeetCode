class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        sum_time = [0] * (1 << n) # 计算所有子集,包括空集
        for s in range(1 << n): 
            for j in range(n):
                if (s >> j) & 1:
                    sum_time[s] += tasks[j]

        # @cache
        # def dfs(left:int) -> int:
        #     if left == 0: return 0
        #     res = inf
        #     s = left
        #     while s:
        #         if sum_time[s] <= sessionTime:
        #             days = 1 + dfs(left ^ s)
        #             res = min(res, days)
        #         s = (s - 1) & left # 下一个合法子集
        #     return res

        # return dfs((1 << n) - 1)

        f = [0] * (1 << n)
        for left in range(1, 1 << n): # left对应dfs(left) 从1开始 因为left == 0: return 0
            res = inf
            s = left
            while s:
                if sum_time[s] <= sessionTime:
                    days = 1 + f[left ^ s] # 改成f的结果
                    res = min(res, days)
                s = (s - 1) & left # 下一个合法子集
            f[left] = res # 对应return res
        return f[-1]
