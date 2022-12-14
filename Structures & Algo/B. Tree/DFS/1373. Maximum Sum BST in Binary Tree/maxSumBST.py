# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        s = 0
        def dfs(node):
            if node is None:
                return math.inf, -math.inf, 0
            
            l_min, l_max, l_sum = dfs(node.left)
            r_min, r_max, r_sum = dfs(node.right)

            if l_max >= node.val or r_min <= node.val:
                return -math.inf, math.inf, 0

            cur = l_sum + r_sum + node.val
            nonlocal s
            s = max(cur, s)
            return min(l_min, node.val), max(r_max, node.val), cur 
            
        dfs(root)
        return s