# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(root):
            if root is None:
                return [0, 0]
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            withRoot = root.val + left[1] + right[1]
            withoutRoot = max(left[0], left[1]) + max(right[0], right[1])
            
            return [withRoot, withoutRoot]
        
        return max(dfs(root))