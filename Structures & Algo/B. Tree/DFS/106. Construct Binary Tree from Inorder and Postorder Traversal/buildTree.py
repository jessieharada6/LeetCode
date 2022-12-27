# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def dfs(postorder, inorder, left, right):
            if left == right: return None
            
            root_val = postorder.pop() 
            idx = inorder.index(root_val)
            root = TreeNode(root_val)
            
            root.right = dfs(postorder, inorder, idx + 1, right)
            root.left = dfs(postorder, inorder, left, idx)
            
            return root
        return dfs(postorder, inorder, 0, len(inorder))

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder: return None
        root = TreeNode(postorder[-1])
        # if len(postorder) == 1: return root
        root_idx = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:root_idx], postorder[:root_idx])
        root.right = self.buildTree(inorder[root_idx + 1:], postorder[root_idx: len(postorder) - 1])
        return root