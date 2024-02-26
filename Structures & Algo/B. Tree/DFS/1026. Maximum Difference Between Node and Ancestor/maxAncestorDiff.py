class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node, path):
            if node is None:
                return
            
            nonlocal ans
            for ele in path:
                ans = max(ans, abs(node.val - ele))
            path.append(node.val)
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
        dfs(root, [])
        return ans
        