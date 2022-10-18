class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        gd, cnt = 0, Counter()
        
        for num in nums:
            gd += cnt[num]
            cnt[num] += 1
        
        return gd
            