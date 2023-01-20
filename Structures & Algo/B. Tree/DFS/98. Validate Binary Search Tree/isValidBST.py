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
                # 保证不进入if条件
                return math.inf, -math.inf
            
            l_min, l_max = dfs(node.left)
            r_min, r_max = dfs(node.right)

            if l_max >= node.val or r_min <= node.val:
                # 找到后返回下面的代码 每一个之后的节点都会进入这个条件 这样可以保证结果归到root
                return -math.inf, math.inf
            
            # node.val应该是左边的l_max 右边的r_min
            return min(l_min, node.val), max(node.val, r_max)
            
        return dfs(root)[0] != -math.inf
###

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(lower, node, upper) -> bool:
            if node is None: return True

            if lower >= node.val or upper <= node.val:
                return False
            
            # 上限用node.val
            return dfs(lower, node.left, node.val) and dfs(node.val, node.right, upper)
        
        return dfs(-math.inf, root, math.inf)

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