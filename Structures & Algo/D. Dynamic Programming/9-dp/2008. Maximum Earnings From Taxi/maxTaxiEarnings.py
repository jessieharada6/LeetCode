class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        n = len(rides)
        
        rides = sorted(rides, key=lambda x: x[1]) # sort end 
        ends = [r[1] for r in rides]

        f = [0] * (n + 1)
        for i in range(n):
            s, e, t = rides[i]
            tips = e - s + t
            last = self.find(s, ends) # find idx so that rides[last] <= current s
            # last is -1 if there is no idx so that rides[last] <= current s
            # f[last + 1] = 0 as f[0] is 0
            f[i + 1] = max(f[i], f[last + 1] + tips) # skip cur ride - f[i], choose cur ride - f[last] + tips
        return f[-1]

    def find(self, target, nums):
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] <= target:
                l = m + 1
            else:
                r = m - 1
        
        return l - 1
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        dist = defaultdict(list)
        for s, e, t in rides:
            dist[e].append((s, e - s + t))
        
        # @cache
        # def dfs(end):
        #     if end == 0: return 0
        #     if end == n + 1: return 0
        #     res = 0
        #     for s, d in dist[end]:
        #         res = max(res, dfs(s) + d) # dfs(s) 上一个终点的最大值
        #     res = max(res, dfs(end - 1)) # ???
        #     return res

        # return max(dfs(end) for end in range(1, n + 1))

        f = [0] * (n + 1)
        for end in range(1, n + 1):
            for start, d in dist[end]:
                f[end] = max(f[end], f[start] + d)
            f[end] = max(f[end], f[end - 1])
        return f[-1]
    
        f = [0] * (n + 1)
        for cur in range(1, n + 1):
            for s, earn in dist[cur]:
                f[cur] = max(f[cur], earn + f[s])
            f[cur] = max(f[cur], f[cur - 1])
        
        return f[-1]
        