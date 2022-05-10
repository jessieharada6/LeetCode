# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = TreeNode(-inf)
        self.first = None
        self.second = None
        
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def swap(root):
            if root is None:
                return root

            swap(root.left) 
            
            if self.prev.val > root.val:
                if self.first == None:
                    self.first = self.prev
                self.second = root            
            self.prev = root # inorder produces ascending values for BST ([3,1,null,null,2] -> 1, 2, 3)
            
            swap(root.right)
            
            return root
        
        swap(root)
        self.first.val, self.second.val = self.second.val, self.first.val