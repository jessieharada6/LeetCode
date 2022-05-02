# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        if root is None:
            return              # as the method returns None
        
                                # if using preorder, 
                                # need to check if every root.left is not null
                                # and go through the while loop below each time
        self.flatten(root.left)
        self.flatten(root.right)

                                # flattened left and right tree
        
        l = root.left
        r = root.right
                                
        root.left = None        
        root.right = l          # root connects to the left
        
        while root.right:
            root = root.right   # traverse 
                                # find the next position
        root.right = r          # connect the right side of the tree