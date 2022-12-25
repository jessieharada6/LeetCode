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
        def dfs(node, cnt): # no return 
            nonlocal ans
            ans = max(ans, cnt)
            if node.left:
                dfs(node.left, cnt + 1 if node.val + 1 == node.left.val else 1)
            if node.right:
                dfs(node.right, cnt + 1 if node.val + 1 == node.right.val else 1)
            
        dfs(root, 1)
        return ans


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node): # return max nodes of left/right
            nonlocal ans
            if node is None: return 0
            l = dfs(node.left)
            r = dfs(node.right)

            if node.left and node.val + 1 == node.left.val:
                l += 1
            else:
                l = 1
            if node.right and node.val + 1 == node.right.val:
                r += 1
            else:
                r = 1
            
            ans = max(ans, max(l, r))
            return max(l, r)
        dfs(root)
        return ans
