# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ans = False
        def dfs(node, path) -> int:
            nonlocal ans
            if node is None: return 0

            path += node.val
            if node.left is node.right and path == targetSum:
                ans = True

            dfs(node.left, path)
            dfs(node.right, path)
        
        dfs(root, 0)
        return ans

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ans = False
        def dfs(node, targetSum):
            nonlocal ans
            if node is None: return 0
            targetSum -= node.val
            if node.left is node.right and targetSum == 0:
                ans = True
            
            dfs(node.left, targetSum)
            dfs(node.right, targetSum)
        
        dfs(root, targetSum)
        return ans