# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, isLeft):
            if node is None: return

            if node.left is node.right and isLeft: 
                nonlocal ans
                ans += node.val
            dfs(node.left, True)
            dfs(node.right, False)
        
        dfs(root, False)
        return ans

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, isLeft):
            if node is None: return 0
            dfs(node.left, True)
            dfs(node.right, False)
            if isLeft and node.left is node.right:
                nonlocal ans
                ans += node.val
            
        dfs(root, False)
        return ans