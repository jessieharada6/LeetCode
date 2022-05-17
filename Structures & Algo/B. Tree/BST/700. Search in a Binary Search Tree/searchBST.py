# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# use for bst, binary search logic - O(logn)
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return
        
        if root.val == val:
            return root
        
        if root.val > val:
            return self.searchBST(root.left, val)
        
        if root.val < val:
            return self.searchBST(root.right, val)


# use for all binary trees, O(n)
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return
        
        if root.val == val:
            return root
        
        left = self.searchBST(root.left, val)
        right = self.searchBST(root.right, val)
        
        return left if left is not None else right