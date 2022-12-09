# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None: 
                return -math.inf, math.inf

            l_max, l_min = dfs(node.left)
            r_max, r_min = dfs(node.right)
            print(node.val, l_max, l_min, r_max, r_min)
            if l_max >= node.val or r_min <= node.val:
                return math.inf, -math.inf
            return max(r_max, node.val), min(l_min, node.val)
        
        return dfs(root)[1] != -math.inf

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