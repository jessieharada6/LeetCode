# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"] 
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def dfs(node, path):
            if node is None: return
            if node.left is node.right:  # leaf node
                path += str(node.val)
                ans.append(path)
                return
            path += str(node.val) + "->"
            dfs(node.left, path)
            dfs(node.right, path)
        
        dfs(root, "")
        return ans

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node):
            if node is None: return []
            if node.left is node.right: return [[str(node.val)]]

            l = dfs(node.left)
            r = dfs(node.right)

            res = []
            for n in l + r:
                res.append(n + [str(node.val)])

            return res

        ans = []
        for nodes in dfs(root):
            ans.append("->".join(map(str,nodes[::-1])))
        
        return ans     

# Output: ["5->2->1","3->1"]
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node):
            if node is None: return []
            if node.left is node.right: return [str(node.val)]

            l = dfs(node.left)
            r = dfs(node.right)

            res = []
            for n in l + r:
                res.append(n + "->" + str(node.val))

            return res

        return dfs(root)

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node):
            res = []
            if node is None: return res
            if node.left is node.right: return [str(node.val)]

            l = dfs(node.left)
            r = dfs(node.right)

            
            for n in l + r:
                res.append(n + "->" + str(node.val))

            return res

        return dfs(root)

# sum from bottom up
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            ans = 0
            if node is None: return ans

            l = dfs(node.left)
            ans += node.val
            r = dfs(node.right)

            return ans + l + r
            
        return dfs(root)