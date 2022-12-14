# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            nonlocal k
            ans = -1
            if node is None: return ans

            l = dfs(node.left)
            k -= 1
            if k == 0:
                ans = node.val
            # print(k, node.val, ans)
            r = dfs(node.right)

            # print("l,r", node.val, l, r)
            if l != -1: return l
            if r != -1: return r
            return ans
            
        return dfs(root)

        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        def dfs(node):
            nonlocal k
            if node is None: return

            dfs(node.left)
            k -= 1
            if k == 0:
                nonlocal ans
                ans = node.val
            dfs(node.right)
            
        
        dfs(root)
        return ans