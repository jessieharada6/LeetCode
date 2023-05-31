# i 固定的, j是排列时的下标 - left的长度会随着i(层数的增加)而变小(left ^ (1<<j)用这个拿走left里的集合,left.bit_count()计算省了几个是1的bit)
# nums[j] & slots[i] 第i个bucket装哪个鸡蛋
# nums[i] & slots[j] 第i个鸡蛋放哪个bucket

# 优化2 用algebra：根据j当前的位置算出对应的slot的数字
class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        n = len(nums)
        m = 2 * numSlots

        @cache
        def dfs(left):
            i = m - left.bit_count()
            if i == n: return 0
            res = 0
            for j in range(m):
                if (left >> j) & 1:
                    andSum = (nums[i] & (1 + j//2)) + dfs(left ^ (1<<j)) 
                    # slots[j] = (1 + j//2) => 
                    # [0，1，2，3，4，5，6，7] index
                    # [1，1，2，2，3，3，4，4] value
                    res = max(res, andSum)
            return res

        return dfs((1 << m) - 1)


# 优化1 - if i == n: return 0 一旦nums里没数字了就不再继续 返回0
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
            i = m - left.bit_count()
            if i == n: return 0
            res = 0
            for j in range(m):
                if (left >> j) & 1:
                    andSum = (nums[i] & slots[j]) + dfs(left ^ (1<<j)) 
                    res = max(res, andSum)
            return res

        return dfs((1 << m) - 1)

        
# 往nums里添0 使其与1879类似
class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        n = len(nums)
        m = 2 * numSlots
        for i in range(2 * numSlots - n):
            nums.append(0)
        slots = [1] # 递推
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