
class Solution:
    def largestSumOfAverages(self, nums: List[int], K: int) -> float:
        n = len(nums)
        psum = [0] # prefix sum
        for num in nums:
            psum.append(psum[-1] + num)

        @cache
        def dfs(left, k):
            if k == 1: return (psum[n] - psum[left]) / (n - left)   
            return max(((psum[nextLeft] - psum[left]) / (nextLeft - left)) + dfs(nextLeft, k - 1) 
                        for nextLeft in range(left + 1, n - k + 2))
        
        return dfs(0, K)

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        def getAverage(l, r):
            return sum(nums[l: r + 1]) / (r - l + 1)

        @cache
        def dfs(left, k):
            if k == 1: return getAverage(left, n - 1)  
            res = 0
            s = 0
            for nextLeft in range(left + 1, n - k + 2):
                s += nums[nextLeft - 1]
                res = max(res, s / (nextLeft - left) + dfs(nextLeft, k - 1))
            return res
        
        return dfs(0, k)
    
class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        def getAverage(l, r):
            return sum(nums[l: r + 1]) / (r - l + 1)

        @cache
        def dfs(left, k):
            if k == 1: return getAverage(left, n - 1)
            return max(getAverage(left, nextLeft - 1) + dfs(nextLeft, k - 1) for nextLeft in range(left + 1, n - k + 2))
        
        return dfs(0, k)
