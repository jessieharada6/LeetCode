class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort() #虽说i < j 但是因为是绝对值 其实无所谓
        def check(m):
            cnt = 0
            j = 0
            for i in range(1, len(nums)):
                while nums[i] - nums[j] > m:
                    j += 1
                cnt += (i - j) # distance of (i - j) is number of pairs that is <= m
            return cnt >= k
        
        l, r = -1, max(nums) - min(nums) # false, true
        while l + 1 < r:
            m = (l + r) // 2
            if check(m):
                r = m
            else:
                l = m

        return r