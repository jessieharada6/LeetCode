# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getNumberOfNodesForEachNode(self, root: Optional[TreeNode]) -> int:
        def t(root):
            if root is None:
                return 0
            
            l = t(root.left)
            r = t(root.right)
            print(f"node of {root.val} has {l} left nodes and {r} right nodes")
            return l + r + 1  # as it is leaving current node, going back to the node above, so count the current node + 1
        
        t(root)              