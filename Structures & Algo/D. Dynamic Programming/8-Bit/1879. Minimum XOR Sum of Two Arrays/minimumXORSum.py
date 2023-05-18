class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        # nums2用全排列方式
        n = len(nums2)
        @cache
        def dfs(idx) -> int: #在剩余元素idx->get最小的xor
            if len(idx) == 0:
                return 0
            res = inf
            i = n - len(idx) # 当前层数
            for idx_i, j in enumerate(idx):
                cur = (nums1[i] ^ nums2[j]) + dfs(idx[:idx_i] + idx[idx_i + 1:])
                res = min(res, cur)
            return res
             
        return dfs(tuple(range(n)))