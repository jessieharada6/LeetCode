# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = TreeNode(-inf)
        self.node = None
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root):
            if root is None:
                return
            
            valid(root.left)
            
            if self.prev.val >= root.val:       # as inorder traversal returns ascending values if BST
                                                # this question defines equal values as false
                if self.node is None:           # if node is assigned a value, it is not BST
                    self.node = self.prev
            self.prev = root
            
            valid(root.right)
        
        valid(root)
        return self.node is None
            