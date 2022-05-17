# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        
        if root.val == key:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            # 1. find the most left (min) on right tree
            node = root.right
            while node.left:
                node = node.left
            # 2. root.left is added at the most left node's left
            node.left = root.left
            # 3. to-be-deleted-root is its right tree
            # not node as it's been traversed to the most left on right tree
            root = root.right           
        
        return root