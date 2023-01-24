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
            if node is None: return

            nonlocal cur_depth
            nonlocal ans
            
            if cur_depth < depth:
                cur_depth = depth
                ans = 0            # reset if cur_depth < depth
            if cur_depth == depth:
                ans += node.val
        
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 1)
        return ans
