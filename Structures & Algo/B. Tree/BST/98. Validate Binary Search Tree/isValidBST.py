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

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = -inf
        invalid = None
        
        def traverse(root):
            nonlocal prev
            nonlocal invalid
            if root is None:
                return
            
            traverse(root.left)
            if prev >= root.val and invalid is None:        
                invalid = prev                              
            prev = root.val
            traverse(root.right)        
        
        traverse(root)
        return invalid is None


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidBST(root, lower, upper):
            if root is None:
                return True
            
            if root.val <= lower or root.val >= upper:
                return False
            
            # to the left tree, max val should be the root val
            # to the right tree, min val should be the root val
            return isValidBST(root.left, lower, root.val) and isValidBST(root.right, root.val, upper) 
            
        return isValidBST(root, -inf, inf)          # set the boundary
            