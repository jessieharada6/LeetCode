# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        count = collections.Counter()
        count[0] = 1

        def dfs(node, s):
            nonlocal ans
            if node is None: return 0
            s += node.val
            if s == targetSum: 
                ans += count[0]
            else: 
                ans += count[s - targetSum]
            count[s] += 1

            dfs(node.left, s)
            dfs(node.right, s)
            count[s] -= 1

        dfs(root, 0)
        return ans