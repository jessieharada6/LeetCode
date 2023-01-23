# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        set_diff = set()
        existence = False

        def dfs(node):
            if node is None: return
            
            if (k - node.val) in set_diff: # 枚举右边的变量
                nonlocal existence   ###
                existence = True

            set_diff.add(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return existence