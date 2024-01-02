class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def getOps(m, nums):
            ops = 0
            for ball in nums:
                if ball > m:
                    ops += (ball - 1) // m
            return ops

        l, r = 0, max(nums) #nnnyyy
        while l + 1 < r:
            m = (l + r) // 2
            if getOps(m, nums) <= maxOperations:
                r = m
            else:
                l = m
        
        return r