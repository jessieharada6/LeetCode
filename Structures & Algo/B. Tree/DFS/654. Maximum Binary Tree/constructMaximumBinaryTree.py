class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(l, r, nums):
            if l == r: return None
            cur_max, cur_idx = -1, -1
            for i in range(l, r):
                if nums[i] > cur_max:
                    cur_max = nums[i]
                    cur_idx = i
            
            root = TreeNode(val = cur_max)
            root.left = dfs(l, cur_idx, nums)
            root.right = dfs(cur_idx + 1, r, nums)

            return root
        
        return dfs(0, len(nums), nums)