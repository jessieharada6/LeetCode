class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = Counter()
        gd = 0
        for i, n in enumerate(nums):
            gd += cnt[n]
            cnt[n] += 1
        
        return gd