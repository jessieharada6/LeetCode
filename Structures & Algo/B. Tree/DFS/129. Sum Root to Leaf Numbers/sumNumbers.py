# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, s):
            if not node: return 0
            s = s * 10 + node.val
            if not node.left and not node.right:
                nonlocal ans
                ans += s
                return
            
            dfs(node.left, s)
            dfs(node.right, s)
                
        
        dfs(root, 0)
        return ans
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, s):
            if not node: return 0
            if not node.left and not node.right:
                nonlocal ans
                s += str(node.val)
                ans += int(s)
                return
            
            s += str(node.val)
            dfs(node.left, s)
            dfs(node.right, s)
                
        
        dfs(root, "")
        return ans

# root=[1,2,3]
# sum 2->1, 3->1 = 52
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None: return []
            if node.left is node.right: return [node.val]

            l = dfs(node.left)
            r = dfs(node.right)
            
            s = []
            for n in l + r:
                s.append(n * 10 + node.val)
            return s

        return sum(dfs(root))