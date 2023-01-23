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


class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(lower, node, upper):
            if node is None:
                return math.inf, -math.inf, 0

            l_min, l_max, l_sum = dfs(lower, node.left, node.val)
            r_min, r_max, r_sum = dfs(node.val, node.right, upper)
            
            if l_max >= node.val or r_min <= node.val:
                return -math.inf, math.inf, 0

            nonlocal ans
            ans = max(ans, l_sum + node.val + r_sum)
            return min(l_min, node.val), max(r_max, node.val), l_sum + node.val + r_sum
        
        dfs(-math.inf, root, math.inf)
        return ans