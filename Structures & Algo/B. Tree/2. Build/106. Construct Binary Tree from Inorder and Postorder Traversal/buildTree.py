# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0 or len(postorder) == 0:
            return
        
        root_val = postorder.pop()
        root_index = inorder.index(root_val)
        
        root = TreeNode(root_val)
        # postorder: left, right, mid - so when we build tree, build right tree, then build left tree
        root.right = self.buildTree(inorder[root_index+1:], postorder)  
        root.left = self.buildTree(inorder[:root_index], postorder)
        
        return root      

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(inorder, postorder, l, r):
            if l == r:
                return

            root_val = postorder.pop()
            root_index = inorder.index(root_val)

            root = TreeNode(root_val)
            root.right = build(inorder, postorder, root_index + 1, r)  
            root.left = build(inorder, postorder, l, root_index)

            return root      
        
        return build(inorder, postorder, 0, len(inorder))