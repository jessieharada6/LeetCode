class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n - 1) // 2
        cnt = Counter()
        gd = 0
        
        for i, x in enumerate(nums):
            x -= i
            gd += cnt[x]
            cnt[x] += 1
        
        return total - gd