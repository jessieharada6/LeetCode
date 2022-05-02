# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        temp = root.left
        root.left = root.right
        root.right = temp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
 
        return root

# it is okay to traverse in preorder or postorder 
# it is not okay to traverse in inorder
    # because after finishing traversing left tree, we swap left and right tree
    # at this point, right tree is not traversed yet
    # once again, we traverse the left tree