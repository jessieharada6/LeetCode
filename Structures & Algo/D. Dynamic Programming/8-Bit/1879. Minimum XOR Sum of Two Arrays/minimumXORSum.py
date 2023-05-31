class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        # nums2用全排列方式
        n = len(nums2)
        @cache
        def dfs(idx) -> int: #在剩余元素idx->get最小的xor
            if len(idx) == 0:
                return 0
            res = inf
            i = n - len(idx) # 当前层数 -- # len(idx) 集合大小
            for idx_i, j in enumerate(idx):
                cur = (nums1[i] ^ nums2[j]) + dfs(idx[:idx_i] + idx[idx_i + 1:])
                res = min(res, cur)
            return res
             
        return dfs(tuple(range(n)))

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        # @cache
        # def dfs(left):
        #     if left == 0: return 0
        #     i = n - left.bit_count()

        #     res = inf
        #     for j in range(n):
        #         if (left >> j) & 1:
        #             cur = (nums1[i] ^ nums2[j]) + dfs(left ^ (1 << j))
        #             res = min(res, cur)
        #     return res
        
        # return dfs((1 << n) - 1)

        f = [0] * (1 << n)
        for left in range(1, 1 << n): # if left == 0: return 0
            i = n - left.bit_count()
            res = inf
            for j in range(n):
                if (left >> j) & 1:
                    cur = (nums1[i] ^ nums2[j]) + f[left ^ (1 << j)]
                    res = min(res, cur)
            f[left] = res
        return f[-1]

##############################3
class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums2)
        # @cache
        # def dfs(left) -> int: 
        #     if left == 0:
        #         return 0
        #     res = inf
        #     i = n - left.bit_count()
        #     for j in range(n):
        #         if (left >> j) & 1:
        #             cur = (nums1[i] ^ nums2[j]) + dfs(left ^ (1 << j))
        #             res = min(res, cur)
        #     return res
             
        # return dfs((1 << n) - 1) #用bits表示下标的位置

        f = [0] * (1 << n) # 用来装结果
        for left in range(1, (1 << n)): # 循环下标
            res = inf
            for j in range(n):
                if (left >> j) & 1:
                    i = n - left.bit_count()
                    cur = (nums1[i] ^ nums2[j]) + f[left ^ (1 << j)]
                    res = min(res, cur)
            f[left] = res
        return f[-1]

        