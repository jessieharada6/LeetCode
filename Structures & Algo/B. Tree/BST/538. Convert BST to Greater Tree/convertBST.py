# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:   
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0
        def greaterTree(root):
            nonlocal total
            if root is None:
                return 0

            # inorder traversal - descending order
            greaterTree(root.right)
            total += root.val
            root.val = total
            greaterTree(root.left)

            return total
        
        greaterTree(root)
        return root
        