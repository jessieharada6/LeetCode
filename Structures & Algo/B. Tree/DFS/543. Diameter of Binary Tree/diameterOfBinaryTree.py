# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.cur = 0
        def depth(root):
            if root is None:
                return 0
            
            l = depth(root.left)
            r = depth(root.right)
            
            self.cur = max(self.cur, l + r)     # every node: left and right side
            
            return max(l, r) + 1                # every node: max depth - either left or right
        
        return depth(root)

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = 0
        def depth(root):
            nonlocal d
            if root is None:
                return 0
            
            l = depth(root.left)
            r = depth(root.right)
            
            d = max(d, l + r)
            
            return max(l, r) + 1
        depth(root)
        return d