# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = defaultdict(TreeNode)
        def dp(root):
            if not root:
                return 0
            
            if root in memo:
                return memo[root]
            
            rob = root.val \
            + (dp(root.left.left) + dp(root.left.right) if root.left else 0) \
            + (dp(root.right.left) + dp(root.right.right) if root.right else 0)

            not_rob = dp(root.left) + dp(root.right)
            
            memo[root] = max(rob, not_rob)
            return memo[root]
        
        return dp(root)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dp(root):
            if not root:
                return [0, 0]
            
            left = dp(root.left)
            right = dp(root.right)
            
            rob = root.val + left[0] + right[0]
            not_rob = max(left[0], left[1]) + max(right[0], right[1])
            
            return [not_rob, rob]
        
        return max(dp(root)[0], dp(root)[1])
        