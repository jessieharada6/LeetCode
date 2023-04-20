# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -inf
        def dfs(node):
            if node is None: return 0

            l = dfs(node.left)
            r = dfs(node.right)

            nonlocal ans
            ans = max(ans, l + r + node.val)
            return max(max(l, r) + node.val, 0) # 左右+当前val如果<0,那一段归为0
        dfs(root)
        return ans
    
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -inf
        def dfs(node): # 返回bu包含当前节点本身的最大值
            if node is None: return 0

            # 如果都是正数 那么一定是两条链的数最大
            # 由于有负数 当是负数时 reset为0
            # 那么依然是两条链+node.val最大
            l = max(0, dfs(node.left)) + node.val
            r = max(0, dfs(node.right)) + node.val

            nonlocal ans
            # 这里减去多出来的一个node.val
            ans = max(ans, l + r - node.val)
            return max(l, r)
        
        dfs(root)
        return ans