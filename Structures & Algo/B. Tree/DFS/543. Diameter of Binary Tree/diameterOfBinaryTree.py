# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0 #左右路径总和
        @cache
        def dfs(node): #返回在当前节点最长的路径 （来自左路径或右路径）
            if node is None: return -1

            l = dfs(node.left) + 1
            r = dfs(node.right) + 1

            nonlocal ans
            ans = max(ans, l + r)
            return max(l, r)
        
        dfs(root)
        return ans
    
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.cur = 0
        def depth(root):
            if root is None:
                return 0
            
            l = depth(root.left)
            r = depth(root.right)
            
            self.cur = max(self.cur, l + r)     # every node: left and right side
            
            return max(l, r) + 1                # every node: max depth - either left or right
        
        return depth(root)

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = 0
        def depth(root):
            nonlocal d
            if root is None:
                return 0
            
            l = depth(root.left)
            r = depth(root.right)
            
            d = max(d, l + r)
            
            return max(l, r) + 1
        depth(root)
        return d