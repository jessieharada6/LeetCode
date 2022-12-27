# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(preorder, inorder, left, right):
            if left == right: return None
            root_val = preorder.pop(0)
            idx = inorder.index(root_val)
            root = TreeNode(root_val)
            root.left = dfs(preorder, inorder, left, idx)
            root.right = dfs(preorder, inorder, idx + 1, right)
            return root
        return dfs(preorder, inorder, 0, len(inorder))

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None
        root = TreeNode(preorder[0])
        # if len(preorder) == 1: return root
        root_idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:root_idx + 1], inorder[:root_idx])
        root.right = self.buildTree(preorder[root_idx + 1:], inorder[root_idx + 1:])
        return root