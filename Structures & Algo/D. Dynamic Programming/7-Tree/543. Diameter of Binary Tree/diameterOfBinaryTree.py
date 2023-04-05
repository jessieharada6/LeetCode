# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            if node is None: return -1

            l = dfs(node.left) + 1
            r = dfs(node.right) + 1

            nonlocal ans
            # print(l, r, node.val)
            ans = max(ans, l + r) # 由ans保存最深的左右深度的和
            return max(l, r)  # 最大深度返回给l,或r
        
        dfs(root)
        return ans
