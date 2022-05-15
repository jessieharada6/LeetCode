# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        path_sum = -inf
        
        def oneSideMax(root):
            nonlocal path_sum
            
            if root is None:
                return 0
            
            # if l or r goes into negative, stop as 0 e.g. [2,-1]
            l = max(0, oneSideMax(root.left))
            r = max(0, oneSideMax(root.right))
            
            path_sum = max(path_sum, l + r + root.val)
            # print(path_sum, root.val)
            
            return max(l, r) + root.val
        
        oneSideMax(root)
        return path_sum