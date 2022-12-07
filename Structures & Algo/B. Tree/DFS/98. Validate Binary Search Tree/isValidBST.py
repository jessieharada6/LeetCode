# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root.left is root.right: return True

        def dfs(node, lower, upper):
            if node is None: 
                return True
            
            l = dfs(node.left, lower, node.val)
            r = dfs(node.right, node.val, upper)

            if lower >= node.val or node.val >= upper:
                return False
            return l and r
    
        return dfs(root, -math.inf, math.inf)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(lower, node, upper) -> bool:
            if not node: return True
            if lower >= node.val or upper <= node.val:
                return False
            return dfs(lower, node.left, node.val) and dfs(node.val, node.right, upper)
        
        return dfs(-math.inf, root, math.inf)