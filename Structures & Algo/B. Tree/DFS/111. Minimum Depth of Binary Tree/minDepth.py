# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        if root.left is root.right: return 1
        # 当 当前节点没有左孩子 当前节点会是1 会变成min 所以给-inf
        l = self.minDepth(root.left) if root.left else -inf
        r = self.minDepth(root.right) if root.right else -inf
        print(root.val, l, r)
        return min(l, r) + 1

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node) -> int:
            if not node: return 0
            if node.left is node.right: return 1

            l = dfs(node.left)
            r = dfs(node.right)

            if l == 0 and r != 0:
                return r + 1
            if l != 0 and r == 0:
                return l + 1
            return min(l, r) + 1 
        
        
        return dfs(root)
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node) -> int:
            if not node: return 0
            if not node.left: 
                return dfs(node.right) + 1
            if not node.right: 
                return dfs(node.left) + 1
            
            l = dfs(node.left)
            r = dfs(node.right)
            return min(l, r) + 1
        
        return dfs(root)