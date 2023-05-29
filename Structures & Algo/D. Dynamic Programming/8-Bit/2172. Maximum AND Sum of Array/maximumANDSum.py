class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        n = len(nums)
        m = 2 * numSlots
        for i in range(2 * numSlots - n):
            nums.append(0)
        slots = [1]
        for i in range(1, m):
            if i % 2:
                slots.append(slots[-1]) 
            else:
                slots.append(slots[-1] + 1)

        @cache
        def dfs(left):
            if left == 0: return 0

            i = m - left.bit_count()
            res = 0
            for j in range(m):
                if (left >> j) & 1:
                    andSum = (nums[j] & slots[i]) + dfs(left ^ (1<<j))
                    res = max(res, andSum)
            return res

        return dfs((1 << m) - 1)