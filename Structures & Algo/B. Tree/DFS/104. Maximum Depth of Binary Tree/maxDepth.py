# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        
        return max(l, r) + 1
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxLevel(root):
            if root is None:
                return 0

            l = maxLevel(root.left)
            r = maxLevel(root.right)
            
            return max(l, r) + 1
        
        return maxLevel(root)