class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        @cache
        def dfs(i, j):
            if i < 0 or j < 0: return -inf
            # 保证每个组合都有
            # dfs(i - 1, j), dfs(i, j - 1) 选nums1(i - 1) 或 nums2(j - 1) 等待到达dfs(i - 1, j - 1)算结果
            # dfs(i - 1, j - 1) + nums1[i] * nums2[j] 两个都选 有product
            # nums1[i] * nums2[j] 前面都不要了
            return max(dfs(i - 1, j), dfs(i, j - 1), dfs(i - 1, j - 1) + nums1[i] * nums2[j], nums1[i] * nums2[j])
        return dfs(n - 1, m - 1)