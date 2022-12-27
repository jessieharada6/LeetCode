# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        ans = 0
        cur = 0
        def dfs(node, depth):
            if not node: return 0

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

            nonlocal cur
            nonlocal ans

            if depth > cur:
                cur = depth
                ans = 0
            if depth == cur:
                ans += node.val
        
        dfs(root, 0)
        return ans
