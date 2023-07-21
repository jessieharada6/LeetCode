class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        payment = []
        for i in range(n):
            payment.append([startTime[i], endTime[i], profit[i]])
        
        payment = sorted(payment, key=lambda x: x[1]) # sort end 
        ends = [r[1] for r in payment]

        f = [0] * (n + 1)
        for i in range(n):
            s, e, t = payment[i]
            last = self.find(s, ends) # find idx so that rides[last] <= current s
            # last is -1 if there is no idx so that rides[last] <= current s
            # f[last + 1] = 0 as f[0] is 0
            f[i + 1] = max(f[i], f[last + 1] + t) # skip cur ride - f[i], choose cur ride - f[last] + tips
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