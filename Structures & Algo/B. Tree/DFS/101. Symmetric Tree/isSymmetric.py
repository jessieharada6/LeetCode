# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def traverse(root, flag):
            if root is None:
                return "#"
            
            l = traverse(root.left, flag)
            r = traverse(root.right, flag)
            
            return str(root.val) + "," + l + "," + r if flag is True else str(root.val) + "," + r + "," + l
        
        # symmetric on both structure and values!
        l = traverse(root.left, True)
        r = traverse(root.right, False)
        
        # print(l, "r", r)
        return l == r

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isS(l, r):
            if l is None and r is None:
                return True
            if l is None or r is None:
                return False
            if l.val != r.val:
                return False
            
            return isS(l.left, r.right) and isS(l.right, r.left)        # mirrored
        
        return isS(root.left, root.right)