class Solution:
    # 以i为结尾的严格递增子序列的最长长度
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # @cache
        # def dfs(i):
        #     mx = 1 # 每一次mx是1 因为当前数是一个子序列 结果记在return里面
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             mx = max(mx, dfs(j) + 1)  # j本来就比i小 不用j - 1
        #     return mx
        # return max(dfs(i) for i in range(n)) # 需要提供多个入口 因为最后一个数不一定是最大的-即不一定会组成最长子序列

        f = [0] * n
        for i, x in enumerate(nums):
            mx = 1
            for j in range(i):
                if x > nums[j]:
                    mx = max(mx, f[j] + 1)
            f[i] = mx
        
        return max(f)

# O(nlogn)
# f[i]-在以len(i + 1)的nums数组里，严格递增子序列f中的最小值
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 1

        f = [nums[0]]
        
        for i in range(1, n):
            if nums[i] > f[-1]:
                f.append(nums[i])
            else:
                l, r = 0, len(f) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if f[mid] < nums[i]:
                        l = mid + 1
                    else:
                        r = mid - 1
                f[l] = nums[i]

        return len(f)            
    
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        f = []

        for x in nums:
            l, r = 0, len(f) - 1
            while l <= r:
                mid = (l + r) // 2
                if f[mid] < x:    #mid游走在f里
                    l = mid + 1
                else:
                    r = mid - 1
            if l == len(f):
                f.append(x)  
            else:
                f[l] = x

        return len(f)