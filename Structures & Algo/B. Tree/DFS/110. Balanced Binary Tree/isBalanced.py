# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = 0
        def dfs(node):
            if not node: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            # print(node.val, l, r)
            if abs(l - r) > 1:
                nonlocal ans
                ans = -1
            return max(l, r) + 1
        dfs(root)
        return ans != -1
