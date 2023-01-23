# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False
        if root.left is root.right and targetSum - root.val == 0: 
            return True

        return self.hasPathSum(root.left, targetSum - root.val) \
        or self.hasPathSum(root.right, targetSum - root.val)
        
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False
        targetSum -= root.val
        if root.left is root.right:
            return targetSum == 0
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
        
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