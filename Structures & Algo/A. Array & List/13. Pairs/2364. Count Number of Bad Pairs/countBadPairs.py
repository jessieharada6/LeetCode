class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n - 1) // 2
        
        gd, cnt = 0, Counter()
        for r, num in enumerate(nums):
            v = r - num
            gd += cnt[v]
            cnt[v] += 1
        
        return total - gd