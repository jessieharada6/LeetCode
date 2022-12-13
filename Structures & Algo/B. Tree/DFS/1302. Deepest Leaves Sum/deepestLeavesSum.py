# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        cur_depth = 0
        ans = 0
        def dfs(node, depth):
            if node is None: return 0

            l = dfs(node.left, depth + 1)
            r = dfs(node.right, depth + 1)
            nonlocal cur_depth
            nonlocal ans
            
            if depth > cur_depth:
                cur_depth = depth
                ans = 0
            if depth == cur_depth:
                ans += node.val

            return max(l, r) + 1
        
        dfs(root, 1)
        return ans