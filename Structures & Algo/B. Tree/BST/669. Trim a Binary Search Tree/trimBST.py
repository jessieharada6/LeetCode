# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # note that the given BST is legal
        if root is None:
            return None
        
        if root.val < low:
            # its left tree vals must all be < low
            # return right tree
            return self.trimBST(root.right, low, high)
        
        if root.val > high:
            # its right tree vals must all be > high
            # return left tree
            return self.trimBST(root.left, low, high)
        
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        
        return root