class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node): # -> current longest 
            if node is None: return 0
            
            l = dfs(node.left)
            r = dfs(node.right)

            if node.left and node.left.val != node.val + 1: l = 0
            if node.right and node.right.val != node.val + 1: r = 0

            nonlocal ans
            ans = max(ans, max(l, r) + 1)
            return max(l, r) + 1
        
        dfs(root)
        return ans


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, count): # -> current longest 
            if node is None: return 0
            
            nonlocal ans
            ans = max(ans, count)
            
            if node.left:
                dfs(node.left, count + 1 if node.val + 1 == node.left.val else 1)
            if node.right:
                dfs(node.right, count + 1 if node.val + 1 == node.right.val else 1)
        
        dfs(root, 1)
        return ans