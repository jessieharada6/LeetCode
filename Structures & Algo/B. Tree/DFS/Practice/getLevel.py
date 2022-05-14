# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLevel(self, root: Optional[TreeNode]) -> int:
        def t(root, level):
            if root is None:
                return
            
            print(f"node of {root.val} is at level {level}")
            t(root.left, level + 1)
            t(root.right, level + 1)
        
        t(root, 1)              # count root as level 1