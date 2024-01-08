class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def check(m):
            copy = nums[:]
            for i in range(len(copy) - 1, 0, -1):
                if copy[i] > m: # nums[i] > 0
                    copy[i - 1] += (copy[i] - m)
            # 数组中每一个元素都<= m 水最终溢出到copy[0]
            return copy[0] <= m

        # 叉叉勾勾
        # 边界是猜的答案
        left, right = -1, max(nums) # 不操作最大值就是max(nums)
        while left + 1 < right:
            m = (left + right) // 2
            if check(m):
                right = m #让结果尽量小
            else:
                left = m
        
        return right
