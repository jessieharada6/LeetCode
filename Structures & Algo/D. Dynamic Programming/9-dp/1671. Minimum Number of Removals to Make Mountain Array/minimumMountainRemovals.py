class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def up(end): # cur i is the ending point, return the longest increasing subsequence
            res = 1
            for j in range(end): # end not end + 1, as j does not need to overlap with end
                if nums[j] < nums[end]:
                    res = max(res, up(j) + 1)
            return res
        @cache
        def down(start): # cur i is the starting point, return the longest decreasing subsequence
            res = 1
            for j in range(n - 1, start, -1):
                if nums[j] < nums[start]:
                    res = max(res, down(j) + 1)
            return res
        
        mountain = 0
        for i in range(n):
            if up(i) > 1 and down(i) > 1: # it must go up then down, up(i) = 1 means there is no up, same for down
                mountain = max(up(i) + down(i) - 1, mountain) # -1 because of the shared nums[i]

        return n - mountain