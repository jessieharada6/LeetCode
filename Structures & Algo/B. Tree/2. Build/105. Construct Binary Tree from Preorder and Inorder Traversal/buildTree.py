# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0 or len(preorder) == 0:
            return
        
        root_val = preorder.pop(0)
        root_index = inorder.index(root_val)
        
        root = TreeNode(root_val)
        root.left = self.buildTree(preorder, inorder[:root_index])
        root.right = self.buildTree(preorder, inorder[root_index + 1:])
        
        return root

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(preorder, inorder, l, r):
            if l == r:
                return
            
            root_val = preorder.pop(0)
            root_index = inorder.index(root_val)

            root = TreeNode(root_val)
            root.left = build(preorder, inorder, l, root_index)
            root.right = build(preorder, inorder, root_index + 1, r)

            return root
        
        return build(preorder, inorder, 0, len(inorder))